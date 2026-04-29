from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
# from .forms import usersforms


# # simple about page
# def aboutUs(request):
#     output = request.GET.get('output')
#     return HttpResponse(f"<h2>Result: {output}</h2>")


# # main form view
# def usersform(request):
#     total = 0

#     # form object
#     fn = usersfroms()

#     if request.method == "POST":
#         try:
#             n1 = float(request.POST.get('num1', 0))
#             n2 = float(request.POST.get('num2', 0))

#             total = n1 + n2

#             # redirect (optional)
#             # return redirect(f"/aboutUs/?output={total}")

#         except:
#             total = "Invalid Input"

#     data = {
#         'form': fn,
#         'total': total
#     }

#     return render(request, "Form.html", data)
   
     

# def Home(request):
#     data = {
#         'title': 'Sujan',
#         'msg': 'SUJAN BHAI MAJAMA AAVDI GYU BADHU KE NAY ',
#         'color': 'red',
#         'btn_color': 'green',
#     'padding': '10px 20px',
#     'border': '5px',
#     'text_color': 'white',
#     'btn_text': 'Click me',
#     ###loop mate 
    
#     'clist': [ 'php','java','Django','rust','go'],
#     'student_details': [
#         {'number':'1','name':'sujan','mo_number':'1234567888'},
#         {'number':'2','name':'kri','mo_number':'1234567888'},  
        
        
#  ],
    
     
#          'numbers':[1,2,3,4,5,6,7],
#         'num': 6,
#         'dat' : {'user': 'sujan'},
   
# }
    
    
    
    
    
#     return render (request,"Form.html")

# def aboutUs(request):
 
    
#     return HttpResponse("<b>Welcome to sujan</b>")

# def course(request):
#     return HttpResponse("Welcome to company ")



# def course(request):
    
    
    #  def submitfrom(request):
        
    #     try:
    #         if request.method=="POST":
                
    #             n1=float(request.POST['num1'])
    #             n2=float(request.POST['num2'])
    #             total=n1+n2
                
    #             data={
    #                 'n1':n1,
    #                 'n2': n2,
    #                 'output':total
    #             }
    #             return HttpResponse(total)




    #     except:
    #         pass













# def courseDetails(request,courseId):   ### daynamic mate nu chhe
#     return HttpResponse(courseId)


# def courseDeeps(request,coursename):    ### daynamic mate nu chhe koi bhi string 
#     return HttpResponse(coursename)


# def slugs(request,myslugs):              ### daynamic mate nu chhe  --- aave 
#     return HttpResponse(myslugs)

# def userFrom(request):
#     total=0
#     try:
#         n1=float(request.POST['num1'])
#         n2=float(request.POST['num2'])
#         total=n1+n2
#     except:
#         pass

#     return render(request,"from.html",{'output':total})








# from django.shortcuts import render

# def From(request):
#     name = ""
#     age = ""

#     # POST method થી data લેશું
#     if request.method == "POST":
#         name = request.POST.get("name")
#         age = request.POST.get("age")

#     data = {
#         'name': name,
#         'age': age
#     }

#     return render(request, "from.html", data)



# from django.shortcuts import render

# def Form(request):
    # # 1️⃣ initial values (empty)
    # name = ""
    # email = ""
    # phone = ""
    # gender = ""
    # dob = ""
    # course = ""
    # address = ""

    # 2️⃣ GET method થી data લઈએ
    # if request.method == "GET":
    #     name = request.GET.get("name","")
    #     email = request.GET.get("email","")
    #     phone = request.GET.get("phone","")
    #     gender = request.GET.get("gender","")
    #     dob = request.GET.get("dob","")
    #     course = request.GET.get("course","")
    #     address = request.GET.get("address","")

    # 3️⃣ dictionary બનાવી
    # data = {
    #     # 'name': name,
    #     # 'email': email,
    #     # 'phone': phone,
    #     # 'gender': gender,
    #     # 'dob': dob,
    #     # 'course': course,
    #     # 'address': address
    # }

    # return render(request, "form.html", {
    #     'name': name,
    #     'email': email,
    #     'phone': phone,
    #     'gender': gender,
    #     'dob': dob,
    #     'course': course,
    #     'address': address
        
        
        
        
        
        
        
        
        
        
        
        
        

# def Form(request):
#     # GET data with default empty values
#     name = request.GET.get("name", "")
#     email = request.GET.get("email", "")
#     phone = request.GET.get("phone", "")
#     gender = request.GET.get("gender", "")
#     dob = request.GET.get("dob", "")
#     course = request.GET.get("course", "")
#     address = request.GET.get("address", "")

#     data = {
#         'name': name,
#         'email': email,
#         'phone': phone,
#         'gender': gender,
#         'dob': dob,
#         'course': course,
#         'address': address
#     }

#     return render(request, "form.html", data)









# from django.shortcuts import render

# def Form(request):
#     name = request.POST.get("name")
#     email = request.POST.get("email", "")
#     phone = request.POST.get("phone", "")
#     gender = request.POST.get("gender", "")
#     dob = request.POST.get("dob", "")
#     course = request.POST.get("course", "")
#     address = request.POST.get("address", "")
    
#     url="/aboutUs/?address1={}".format(address)

    
#     return HttpResponseRedirect(url)

#     return render(request, "form.html", {
#         'name': name,
#         'email': email,
#         'phone': phone,
#         'gender': gender,
#         'dob': dob,
#         'course': course,
#         'address1': address 
#     })
































# def calculator(request):
#     c=''
#     n1 = ''
#     n2 = ''
#     try:
#         if request.method=="POST":
#              n1=float(request.POST.get('num1'))
#              n2=float(request.POST.get('num2'))
#              opr=request.POST.get('opr')
#              if opr=='+':
#                 c=n1+n2
#              elif opr=='-':
#                 c=n1-n2
#              elif opr=='*':
#                 c=n1+n2
#              elif opr=='/':
#                 c=n1-n2


#     except :
#         c="invalid opr......"
#     print(c)
 
#     return render(request, 'calculator.html', {
#             'c': c,
#             'n1': n1,
#             'n2': n2
#         })







# def calculator(request):
#     c = ''
#     n1 = ''
#     n2 = ''

#     try:
#         if request.method == "POST":
#             n1 = float(request.POST.get('num1'))
#             n2 = float(request.POST.get('num2'))
#             opr = request.POST.get('opr')

#             if opr == '+':
#                 c = n1 + n2
#             elif opr == '-':
#                 c = n1 - n2
#             elif opr == '*':
#                 c = n1 * n2
#             elif opr == '/':
#                 c = n1 / n2 if n2 != 0 else "Cannot divide by zero"

#     except:
#         c = "Invalid Input"

#     return render(request, 'calculator.html', {
#         'c': c,
#         'n1': n1,
#         'n2': n2
#     })


# from django.shortcuts import render, redirect

# def calculator(request):
#     if request.method == "POST":
#         try:
#             n1 = float(request.POST.get('num1'))
#             n2 = float(request.POST.get('num2'))
#             opr = request.POST.get('opr')

#             if opr == '+':
#                 c = n1 + n2
#             elif opr == '-':
#                 c = n1 - n2
#             elif opr == '*':
#                 c = n1 * n2
#             elif opr == '/':
#                 c = n1 / n2 if n2 != 0 else "Cannot divide by zero"

#             # 👉 redirect kari devu (refresh ma data clear)
#             return redirect('/calculator/')

#         except:
#             return redirect('/calculator/')

#     # 👉 GET request → empty values
#     return render(request, 'calculator.html')



# def calculator(request):
#     c = ''

#     if request.method == "POST":
#         num = request.POST.get('num1')

#         if num == "" or num is None:
#             c = "Please enter number"
#         else:
#             try:
#                 n = float(num)

#                 if n % 2 == 0:
#                     c = "Even"
#                 else:
#                     c = "Odd"

#             except:
#                 c = "Invalid input"

#     return render(request, "calculator.html", {'c': c})
def calculator(request):
    data = {}

    if request.method == "POST":
        try:
            s1 = float(request.POST.get('subject1'))
            s2 = float(request.POST.get('subject2'))
            s3 = float(request.POST.get('subject3'))
            s4 = float(request.POST.get('subject4'))
            s5 = float(request.POST.get('subject5'))

            t = s1 + s2 + s3 + s4 + s5
            p = t * 100 / 500

            if p > 60:
                d = "first"
            elif p > 48:
                d = "second"
            elif p > 35:
                d = "third"
            else:
                d = "fail"

            data = {
                'total': t,
                'per': p,
                'div': d
            }

        except:
            data['error'] = "Invalid Input"

    return render(request, "calculator.html", data)




