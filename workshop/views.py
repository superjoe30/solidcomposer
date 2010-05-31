from opensourcemusic.workshop.models import *
from opensourcemusic.workshop.forms import *
from opensourcemusic.main.models import *
from opensourcemusic.main.views import safe_model_to_dict, json_response
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render_to_response, get_object_or_404

from main.uploadsong import upload_song

def ajax_home(request):
    data = {
        'user': {
            'is_authenticated': request.user.is_authenticated(),
        },
    }

    if request.user.is_authenticated():
        data['user'].update(safe_model_to_dict(request.user))

        # bands the user is a part of
        def band_data(member):
            d = safe_model_to_dict(member.band)
            d['role'] = member.role
            return d
        members = BandMember.objects.filter(user=request.user)
        data['bands'] = [band_data(x) for x in members]

        # invitations
        def invite_data(invite):
            d = safe_model_to_dict(invite)
            d['band'] = safe_model_to_dict(invite.band)
            return d
        invites = BandInvitation.objects.filter(invitee=request.user)
        data['invites'] = [invite_data(x) for x in invites]


    return json_response(data)

def handle_invite(request, accept):
    data = {'success': False}

    invitation_id_str = request.GET.get("invitation", 0)
    try:
        invitation_id = int(invitation_id_str)
    except ValueError:
        invitation_id = 0

    invite = get_object_or_404(BandInvitation, id=invitation_id)

    # make sure the user has permission to reject this invitation
    if invite.invitee != request.user:
        data['reason'] = "This invitation was not sent to you."
        return json_response(data)

    if accept:
        # apply the invitation
        member = BandMember()
        member.user = request.user
        member.band = invite.band
        member.role = invite.role
        member.save()

    invite.delete()
        
    data['success'] = True
    return json_response(data)

@login_required
def ajax_accept_invite(request):
    return handle_invite(request, accept=True)
    
@login_required
def ajax_ignore_invite(request):
    return handle_invite(request, accept=False)

@login_required
def band(request):
    "todo"
    pass

@login_required
def create_band(request):
    "todo"
    pass

@login_required
def project(request, band_id_str, project_id_str):
    "todo"
    pass

@login_required
def create_project(request, band_str):
    band_id = int(band_str)
    band = get_object_or_404(Band, id=band_id)
    err_msg = ''
    if request.method == 'POST':
        form = NewProjectForm(request.POST, request.FILES)
        if form.is_valid():
            prof = request.user.get_profile()

            mp3_file = request.FILES.get('file_mp3')
            source_file = request.FILES.get('file_source')

            # make sure we have not hit the user's quota
            new_used_space = prof.used_space + mp3_file.size + source_file.size
            if new_used_space > prof.total_space:
                err_msg = design.reached_upload_quota
            else:
                # upload the song
                result = upload_song(
                    file_mp3_handle=mp3_file,
                    file_source_handle=source_file, 
                    band=band,
                    song_title=form.cleaned_data.get('title'))
                if not result['success']:
                    err_msg = result['reason']
                else:
                    # fill in the rest of the fields
                    song = result['song']
                    song.owner = request.user
                    song.comments = form.cleaned_data.get('comments', '')
                    song.save()

                    # create the project
                    project = Project()
                    project.band = band
                    project.save()

                    # create the first version
                    version = ProjectVersion()
                    version.project = project
                    version.song = song
                    version.version = 1
                    version.save()

                    # subscribe the creator
                    project.subscribers.add(request.user)
                    project.save()

                    return HttpResponseRedirect(reverse("workbench.project", args=[band.id, project.id]))
    else:
        form = NewProjectForm()
    return render_to_response('workbench/new_project.html', {
            'form': form,
            'err_msg': err_msg,
        }, context_instance=RequestContext(request))
    
