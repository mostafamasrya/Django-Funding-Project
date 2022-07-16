from django.conf import settings
from django.db.models import Max
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import *


# Create your views here.
# def home(request):
#     if request.session.has_key('user_name'):
#         categories = Category.objects.all()
#         context ={'categories':categories}
#         return render(request, 'home.html',context)
#     else:
#         return redirect('login')

def home(request):
    latestProjects = Projects.objects.values('id').order_by('-start_date')[0:5]
    FeaturedProjects = Projects.objects.values('id')[0:5]
    topratedProjects = Rate.objects.values('project').annotate(rate=Max('rate')).order_by('-rate')[0:5]
    latestProjectsList = []
    for project in latestProjects:
        latestProjectsList.append(ProjectsImages.objects.filter(project=project['id'])[0])
    featuredProjectsList = []

    for project in FeaturedProjects:
        featuredProjectsList.append(ProjectsImages.objects.filter(project=project['id'])[0])
    topRatedProjectsList = []

    for project in topratedProjects:
        topRatedProjectsList.append(ProjectsImages.objects.filter(project=project['id'])[0])
    categories = Category.objects.all()
    context = {
        'latestProjectsList': latestProjectsList,
        'categories': categories,
        'featuredProjectsList': featuredProjectsList,
        'topRatedProjectsList': topRatedProjectsList,
    }
    return render(request, "home.html", context)


def add_project(request):
    if request.session.has_key('user_name'):
        if request.method == 'POST':
            user = Usercrowd.objects.filter(id=int(request.session['user_id']))[0]
            category = get_object_or_404(Category, id=request.POST['category'])
            newproject = Projects.objects.create(
                title=request.POST['title'], category=category.title,
                total_target=request.POST['total_target'],
                start_date=request.POST['start_date'], end_date=request.POST['end_date'],
                details=request.POST['details'],user=user
            )

            tags = request.POST['tags']
            list_tags = list(tags.split(" "))
            images = request.FILES.getlist('images')
            if newproject:
                for image in images:
                    photo = ProjectsImages.objects.create(
                        images=image,
                        project=newproject
                    )
                for tag in list_tags:
                    newtag = ProjectsTages.objects.create(
                        tags=tag,
                        project=newproject
                    )

            return redirect('add_project')
        else:
            categories = Category.objects.all()
            context = {'categories': categories}
            return render(request, 'startCampain.html',context)
    else:
        return redirect('login')

def admin_home(request):
    if request.session.has_key('user_name'):
        user = Usercrowd.objects.filter(id=int(request.session['user_id']))[0]
        if user.is_admin == True:
            if request.method == 'POST':
                newcategory = Category.objects.create(
                    title=request.POST['title'], image_cat = request.FILES['image_cat'],
                    user=user
                )
                return redirect('admin')
            else:
                return render(request,'admin.html')
        else:
            return render(request, 'notfounderror.html')
    return redirect('login')

def add5projects(request):
    if request.session.has_key('user_name'):
        user = Usercrowd.objects.filter(id=int(request.session['user_id']))[0]
        if user.is_admin == True:
            if request.method == 'POST':
                projectsAdmin =[]
                if request.POST['pro1']:
                    project1 =Projects.objects.get(id=request.POST['pro1'])
                    projectsAdmin.append(project1)
                if request.POST['pro2']:
                    project2 =Projects.objects.get(id=request.POST['pro2'])
                    projectsAdmin.append(project2)
                if request.POST['pro3']:
                    project3 =Projects.objects.get(id=request.POST['pro3'])
                    projectsAdmin.append(project3)
                if request.POST['pro4']:
                    project4 =Projects.objects.get(id=request.POST['pro4'])
                    projectsAdmin.append(project4)
                if request.POST['pro5']:
                    project5 =Projects.objects.get(id=request.POST['pro4'])
                    projectsAdmin.append(project5)
                # newcategory = Category.objects.create(
                #     title=request.POST['title'], image_cat=request.FILES['image_cat'],
                #     user=user
                # )
                return render(request,'add5Projects.html')
            else:
                projects = Projects.objects.all()
                return render(request,'add5Projects.html',{'projects':projects})
        else:
            return render(request, 'notfounderror.html')
    return redirect('login')


def project_reports(request):
    return render(request,'ProjectsReport.html')

def comments_reports(request):
    return render(request,'commentsReport.html')


def list_projects(request):
    if request.session.has_key('user_name'):
        categories = Category.objects.all()
        projects = Projects.objects.all()
        images = []
        for project in projects:
            img = ProjectsImages.objects.filter(project=project.id)[0]
            images.append(img)
        for image in images:
            print(image.project.title ,image.images)
        context = {
            'categories': categories,
            'images'    : images
        }
        return render(request,'listProjects.html' , context )

def add_report(request):
    return render(request,'Commentreport.html')

def product_details(request):
    return render(request,'Product_details.html')

def project_info(request, id):
    context = {}
    project_data = Projects.objects.get(id=id)
    images = ProjectsImages.objects.filter(project=project_data.id)
    rate = Rate.objects.filter(project=project_data.id)
    donations = Donation.objects.filter(project=project_data.id)
    sum = 0
    count = 0
    for i in rate:
        sum += i.rate
        count += 1
    avg_rate = sum / count
    donation=0
    for d in donations:
        donation = donation + int(d.donation_value)
    context['project'] = project_data
    context['images'] = images
    context['avg_rate'] = avg_rate
    context['donation'] = donation
    user = Usercrowd.objects.filter(id=int(request.session['user_id']))[0]
    if user:
        if request.method == 'GET':
            return render(request, 'Product_details.html', context)
        elif request.method == 'POST':
            Donation.objects.create(project=project_data, donation_value=request.POST['donation_value'],
                                        user=user)
            return redirect(f'/projects/product_details/{project_data.id}')
    else:
        return redirect('login')


# --------------------------------- Add Comment -----------------------------------------

def add_comment(request, id):
    if request.session.has_key('user_name'):
        project = Projects.objects.get(id=id)
        comments = Comment.objects.filter(project=project.id)
        user = Usercrowd.objects.filter(id=int(request.session['user_id']))[0]
        context = {}
        context['project'] = project
        context['comments'] = comments
        context['user'] = user
        if request.method == "GET":
            return render(request, 'Product_details.html', context)

        if request.method == "POST":
            Comment.objects.create(project=project, comment=request.POST['comment'],
                                   user=user)
            return redirect(f'/projects/product_details/{project.id}')
    else:
        return redirect('login')


def add_rate(request, id):
    if request.session.has_key('user_name'):
        project = Projects.objects.get(id=id)
        rate = Rate.objects.filter(project=project.id)
        user = Usercrowd.objects.filter(id=int(request.session['user_id']))[0]

        context = {}
        context['project'] = project
        context['rate'] = rate
        context['user'] = user
        user_rate = Rate.objects.filter(user=user, project=project.id)
        print(user_rate)
        if request.method == "POST":
            if not user_rate:
                Rate.objects.create(project=project, rate=request.POST['rate'],
                                    user=user)

                return redirect(f'/projects/product_details/{project.id}')
            else:
                context['error_msg'] = "You have rated this project before"
                return render(request, 'Product_details.html', context)
    else:
        return redirect('login')


