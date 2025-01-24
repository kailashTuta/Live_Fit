from django.shortcuts import render
from .models import AyurvedicTips
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required(login_url='login')
def ayurvedicTips(request):
    ayurvedicTips = AyurvedicTips.objects.all().order_by('id')
    paginator = Paginator(ayurvedicTips, 12)
    page_num = request.GET.get('page', 1)
    ayurvedicTips = paginator.get_page(page_num)
    context = {'ayurvedicTips': ayurvedicTips}
    return render(request, 'ayurvedic_tips/ayurvedic_tips.html', context)


def tipDetails(request, pk):
    tip = AyurvedicTips.objects.get(pk=pk)
    context = {'tip': tip}
    return render(request, 'ayurvedic_tips/tip_details.html', context)
