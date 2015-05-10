
# Course Selection System

## 1. Instructions
This project targets to create a course-selection-system, which is powered by Django and involving  
AngularJs.

#### Figure 1:
![Design Flow](https://github.com/daihong391/StuManage/raw/master/images/HTMLDesignFlow.png)

The above figure shows the design-flow of the course-selection-system, and it is divided into  
5 parts, Main Page, Administer Page, Teacher Page, Student Page and Course Page.

#### Figure 2:
![Design Flow](https://github.com/daihong391/StuManage/raw/master/images/databaseDesignFlow.png)

The corresponding databases used in the project, is showing as above, and it is divided into  
4 parts, Administer, Teacher, Student and Course.

### 1.1 Environment
This project is developing on Windows 8, and the edition of Django and Python are 1.7.8 and 3.4.3,  
respectively.

## 2. Details
### 2.1 HTML
#### 2.1.1 Main Page
This page mainly focuses on the function for logging into administer account and user account  
(teacher/student). Figure 3 shows the login interface for the administer, and Figure 4 shows  
the similar interface for user accounts.

#### Figure 3:
![Main Page](https://github.com/daihong391/StuManage/raw/master/images/mainPage2.png)
#### Figure 4
![Main Page](https://github.com/daihong391/StuManage/raw/master/images/mainPage1.png)

#### 2.1.2 Administer Page
Logging into this account, there are several functions that an administer can manage this system:  
change own password, add accounts or change password for other users and other administers,    
delete accounts, and manage courses.

#### Figure 5:
![Admin Page](https://github.com/daihong391/StuManage/raw/master/images/adminChangePassword.PNG)

#### Figure 6:
![Admin Page](https://github.com/daihong391/StuManage/raw/master/images/adminCreatingAccounts.PNG)

#### Figure 10:
![Admin Page](https://github.com/daihong391/StuManage/raw/master/images/adminDeleteAccount.PNG)

#### Figure 11:
![Admin Page](https://github.com/daihong391/StuManage/raw/master/images/adminModifyCourses.PNG)

#### 2.1.3 Teacher Page
This section for teacher is divided into two parts: one page for displaying basic information, another for  
modifying account information. 

#### Figure 15:
![Teacher Page](https://github.com/daihong391/StuManage/raw/master/images/TEACHER_BASIC.PNG)

#### Figure 16:
![TEACHER Page](https://github.com/daihong391/StuManage/raw/master/images/TEACHER_MODIFY.PNG)

#### 2.1.4 Student Page
#### Figure 17:
![Student Page](https://github.com/daihong391/StuManage/raw/master/images/STUDENT_BASIC.PNG)

#### Figure 18:
![Student Page](https://github.com/daihong391/StuManage/raw/master/images/STUDENT_MODIFY.PNG)

### 2.2 Database
#### 2.2.1 Administer Table
<table border="1" cellspacing="0">
    <tr>
        <td>
            Column Name
        </td>
        <td>
            Type
        </td>
        <td>
            NULL
        </td>
    </tr>
    <tr>
        <td>
            username
        </td>
        <td>
            email
        </td>
        <td>
            False
        </td>
    </tr>
    <tr>
        <td>
            password
        </td>
        <td>
            varchar(30)
        </td>
        <td>
            False
        </td>
    </tr>
</table>

#### 2.2.2 Course Table
<table border="1" cellspacing="0">
    <tr>
        <td>
            Column Name
        </td>
        <td>
            Type
        </td>
        <td>
            NULL
        </td>
        <td>
            Unique
        </td>
        <td>
            default
        </td>
    </tr>
    <tr>
        <td>
            Course Name
        </td>
        <td>
            varchar(50)
        </td>
        <td>
        </td>
        <td>
            True
        </td>
        <td>
            ""
        </td>
    </tr>
    <tr>
        <td>
            Course Credit
        </td>
        <td>
            Positive Integer
        </td>
        <td>
            
        </td>
        <td>
            
        </td>
        <td>
            
        </td>
    </tr>
    <tr>
        <td>
            Course Hour
        </td>
        <td>
            Positive Integer
        </td>
        <td>
            
        </td>
        <td>
            
        </td>
        <td>
            
        </td>
    </tr>
    <tr>
        <td>
            Course Start
        </td>
        <td>
            DateTime
        </td>
        <td>
            
        </td>
        <td>
            
        </td>
        <td>
            
        </td>
    </tr>
    <tr>
        <td>
            Course Overall People
        </td>
        <td>
            Positive Integer
        </td>
        <td>
            
        </td>
        <td>
            
        </td>
        <td>
            0
        </td>
    </tr>
</table>

#### 2.2.3 Teacher Table
<table border="1" cellspacing="0">
    <tr>
        <td>
            Column Name
        </td>
        <td>
            Type
        </td>
        <td>
            NULL
        </td>
        <td>
            Unique
        </td>
        <td>
            default
        </td>
        <td>
            Foreign Key
        </td>
    </tr>
    <tr>
        <td>
            Teacher Id
        </td>
        <td>
            varchar(30)
        </td>
        <td>
            
        </td>
        <td>
            True
        </td>
        <td>
            ""
        </td>
        <td>
            
        </td>
    </tr>
    <tr>
        <td>
            Teacher Name
        </td>
        <td>
            varchar(30)
        </td>
        <td>
            
        </td>
        <td>
            
        </td>
        <td>
            ""
        </td>
        <td>
           
        </td>
    </tr>
    <tr>
        <td>
            Course
        </td>
        <td>
           
        </td>
        <td>
            
        </td>
        <td>
            
        </td>
        <td>
            
        </td>
        <td>
            True
        </td>
    </tr>
    <tr>
        <td>
            Teacher Password
        </td>
        <td>
           varchar(30)
        </td>
        <td>
            
        </td>
        <td>
            
        </td>
        <td>
            
        </td>
        <td>
            
        </td>
    </tr>
</table>

#### 2.2.4 Student Table
<table border="1" cellspacing="0">
    <tr>
        <td>
            Column Name
        </td>
        <td>
            Type
        </td>
        <td>
            NULL
        </td>
        <td>
            Unique
        </td>
        <td>
            default
        </td>
        <td>
            Foreign Key
        </td>
    </tr>
    <tr>
        <td>
            Student Id
        </td>
        <td>
            varchar(30)
        </td>
        <td>
            
        </td>
        <td>
            True
        </td>
        <td>
            ""
        </td>
        <td>
            
        </td>
    </tr>
    <tr>
        <td>
            Student Name
        </td>
        <td>
            varchar(30)
        </td>
        <td>
            
        </td>
        <td>
            
        </td>
        <td>
            ""
        </td>
        <td>
            
        </td>
    </tr>
    <tr>
        <td>
            Course
        </td>
        <td>
            
        </td>
        <td>
            
        </td>
        <td>
            
        </td>
        <td>
            
        </td>
        <td>
            True
        </td>
    </tr>
    <tr>
        <td>
            Student Password
        </td>
        <td>
            varchar(30)
        </td>
        <td>
            
        </td>
        <td>
            
        </td>
        <td>
            ""
        </td>
        <td>
            
        </td>
    </tr>
</table>

## 3. Steps for Running Project
### 3.1 Download Project from Github
* Select a folder you want to store the project "StuManage"
* Run the "Git Bash"
* Enter "git clone git@github.com:daihong391/StuManage.git"

### 3.2 Creating an Administer Account
* Open Command Prompt Window
* Enter the document which you store the cloned project "StuManage" from Github
* Continue to enter this project, and then input "python manage.py shell"
* Enter "from studentManage.models import Adminer" to invoke the database of administer
* user following two command to create an account:
    * "p=Adminer(username='HONG@126.com', password='111111')"
    * "p.save()"

### 3.3 Starting Server
* Enter "exit()" to quit shell
* Input "python manage.py runserver" to start the Server

### 3.4 Running project
* Open a browser, and input the link "127.0.0.1:8000/mainpage/"
* The main page is divided into two parts, Figure 3 and  
  Figure 4.
#### Figure 3:
![Main Page](https://github.com/daihong391/StuManage/raw/master/images/mainPage2.png)
#### Figure 4
![Main Page](https://github.com/daihong391/StuManage/raw/master/images/mainPage1.png)

* By clicking the bellowing two buttons you can change between each other.
#### Figure 7:
![User](https://github.com/daihong391/StuManage/raw/master/images/userLoginButton.PNG)
#### Figure 8:
![User](https://github.com/daihong391/StuManage/raw/master/images/administerLoginButton.PNG)

#### 3.4.1 Administer Part
* Entering the correct username and password, you will enter the administer page, as  
  Figure 5, 6, 10 and 11.

#### Figure 5:
![Admin Page](https://github.com/daihong391/StuManage/raw/master/images/adminChangePassword.PNG)

#### Figure 6:
![Admin Page](https://github.com/daihong391/StuManage/raw/master/images/adminCreatingAccounts.PNG)

#### Figure 10:
![Admin Page](https://github.com/daihong391/StuManage/raw/master/images/adminDeleteAccount.PNG)

#### Figure 11:
![Admin Page](https://github.com/daihong391/StuManage/raw/master/images/adminModifyCourses.PNG)

* In this part, you can change the password for administer in Figure 5.
* You can also create account for other administer, teacher and student, and change their password  
  in Figure 6.
* In Figure 10, you can delete accounts for other users and administers except yourself.
* Figure 11 shows the interface for managing the course database. Inside this page, you can  
  add a new course, modify it, and delete courses.
    * Figure 12 is for adding a new course
    * Figure 13 is for searching a course and modifying it
    * Figure 14 is for deleting a course

#### Figure 12:
![Admin Page](https://github.com/daihong391/StuManage/raw/master/images/adminAddCourse.PNG)

#### Figure 13:
![Admin Page](https://github.com/daihong391/StuManage/raw/master/images/adminSearchAddCourses.PNG)

#### Figure 14:
![Admin Page](https://github.com/daihong391/StuManage/raw/master/images/adminDeleteCourses.PNG)

* By clicking the bwllowing buttons, you can switch among those four pages.

#### Figure 9:
![Admin Page](https://github.com/daihong391/StuManage/raw/master/images/administerManageButton.PNG)


#### 3.4.2 User Part
* Entering the correct username and password, you can enter either the teacher page or student page  
  including basic information through the login page Figure 4.
* Both student and teacher part, they include one page for showing basic information, and another for  
  modifying account as Figure 15, 16 for teacher and Figure 17,18 for student.
* By click buttons in Figure 19, you can between two pages: the basic and the modify.

#### Figure 19:
![Switch Button](https://github.com/daihong391/StuManage/raw/master/images/SWITCH_BUTTON.PNG)