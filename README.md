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
Logging into this account, the administer can change his own password, add other administer's  
, student's and teacher's accounts. The details are showing inside the bellowing figures.

#### Figure 5:
![Admin Page](https://github.com/daihong391/StuManage/raw/master/images/adminChangePassword.PNG)

#### Figure 6:
![Admin Page](https://github.com/daihong391/StuManage/raw/master/images/adminCreatingAccounts.PNG)

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
            password
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
            max_length
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
            varchar
        </td>
        <td>
            False
        </td>
        <td>
            True
        </td>
        <td>
            50
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
            False
        </td>
        <td>
            False
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
            False
        </td>
        <td>
            False
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
            False
        </td>
        <td>
            False
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
            False
        </td>
        <td>
            False
        </td>
        <td>
            
        </td>
        <td>
            0
        </td>
    </tr>
</table>