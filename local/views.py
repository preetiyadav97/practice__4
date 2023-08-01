from django.shortcuts import render,HttpResponse,redirect
from local.models import Course_detail

# Create your views here.
def first(request):
    show=Course_detail.objects.all()
    print(show)
    Coll = {'show': show}
    return render(request,'index.html',Coll)

def update_place(request,num):
    
    obj = Course_detail.objects.get(id =num)
    print(obj)
    
    
    if request.method == 'POST':
        name = request.POST.get('name')
        Code = request.POST.get('Code')
        Collage = request.POST.get('Collage')   
        Student = request.POST.get('Student')
        
        obj.Coursename = name
        obj.Code = Code
        obj.Collage = Collage
        obj.Student = Student
        obj.save()
        return redirect("update1")



    
   
    data = {"obj": obj}
    
    # return render(request,'uplode.html',data)
    # Coll = {'show': show}
    return render(request,'upload.html',data)

def Create_place(request):
    
    if request.method == 'POST':
       
        name = request.POST['name']
        # print(name)
        Code = request.POST['Code']
        # print(email)
        Collage = request.POST['Collage']  
        # print(salary)
        Student = request.POST['Student']
        # print(lname)
 
        d=Course_detail   (Coursename=name, Code=Code, Collage=Collage, Student=Student)
        d.save()
        return redirect("first1")



    
    
    return render(request,'Create.html')
    
def  Delete_place(request,num):
 
    obj = Course_detail.objects.get(id = num )
    if obj:
        obj.delete()
        return redirect("first1")

    
    
    show=Course_detail.objects.all()
    print(show)
    Coll = {'show': show}
    return render(request,'index.html',Coll)
    
    
