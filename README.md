# NuaaOversea-backend-Flask
NuaaOversea is a studying aboard information sharing platform. You can find out people who have the similar background with you are admitted to which universities and help you make wise decision.

This repository is the backend of NuaaOversea built with **FLASK**

## Get Started

1. Copy the `config.py.sample` and rename it as `config.py`. In this file, you should replace the enviroment params with yours.
2. As a developer, you should `export FLASK_APP=oversea.py` and `flask run` in your command line.
3. If you want to deploy, perhaps, you should run the `oversea.py` with `uwsgi`

## API

### Status Code

- 200 OK - [GET]：服务器成功返回用户请求的数据，该操作是幂等的（Idempotent）。

- 201 CREATED - [POST/PUT/PATCH]：用户新建或修改数据成功。

- 202 Accepted - [*]：表示一个请求已经进入后台排队（异步任务）

- 204 NO CONTENT - [DELETE]：用户删除数据成功。

- 400 INVALID REQUEST - [POST/PUT/PATCH]：用户发出的请求有错误，服务器没有进行新建或修改数据的操作，该操作是幂等的。

- 401 Unauthorized - [*]：表示用户没有权限（令牌、用户名、密码错误）。

- 403 Forbidden - [*] 表示用户得到授权（与401错误相对），但是访问是被禁止的。

- 404 NOT FOUND - [*]：用户发出的请求针对的是不存在的记录，服务器没有进行操作，该操作是幂等的。

- 406 Not Acceptable - [GET]：用户请求的格式不可得（比如用户请求JSON格式，但是只有XML格式）。

- 410 Gone -[GET]：用户请求的资源被永久删除，且不会再得到的。

- 422 Unprocesable entity - [POST/PUT/PATCH] 当创建一个对象时，发生一个验证错误。

- 500 INTERNAL SERVER ERROR - [*]：服务器发生错误，用户将无法判断发出的请求是否成功。

  

### Error handling

When the status code is 4xx, the response is as follow.

```json
{
    error: "error message"
}
```

#### /applications

##### GET

###### response

```json
{
    "applications": [
        {
            "tags": [
                {
                    "id": "2",
                    "name": "转专业"
                }
            ],
            "language_writing": 24,
            "id": "2",
            "language_speaking": 23,
            "language_reading": 21,
            "gre_verbal": 156,
            "applicant_id": 2,
            "country": "德国",
            "major": "IS",
            "language_type": "TOEFL",
            "term": "2018spring",
            "university": "NEU",
            "result": "ad",
            "gpa": 3.4,
            "gre_quantitative": 161,
            "language_listening": 22,
            "gre_writing": 3.5,
            "degree": "Ph.D"
        },
        {
			...
        }
    ]
}
```

##### POST

###### form-data

| Params       | Required | Description |
| ------------ | -------- | ----------- |
| applicant_id | True     |             |
| country_id   | True     |             |
| degree       | True     |             |
| university   | True     |             |
| major        | True     |             |
| term         | True     |             |
| result       | True     |             |
| is_transfer  | True     |             |

###### response

```json
{
    "id": 4
}
```

#### /applications/<application_id>

##### GET

###### response

```json
{
    "gre_quantitative": 161,
    "applicant_id": 2,
    "gpa": 3.4,
    "language_writing": 24,
    "id": "1",
    "term": "2018FALL",
    "language_type": "TOEFL",
    "major": "CS",
    "gre_writing": 3.5,
    "tags": [],
    "recommendation": {
        "value": 4,
        "id": "4",
        "name": "国内牛推"
    },
    "country": "美国",
    "research": {
        "value": 1,
        "id": "1",
        "name": "无科研经历"
    },
    "result": "ad",
    "gre_verbal": 156,
    "project": {
        "value": 3,
        "id": "3",
        "name": "国内大公司实习"
    },
    "language_reading": 21,
    "language_listening": 22,
    "degree": "Master",
    "language_speaking": 23,
    "university": "CMU"
}
```

#### /applicants

##### GET

###### response

```json
{
    "applicants": [
        {
            "gre_quantitative": 150,
            "gre_writing": 3,
            "language_writing": 20,
            "id": 1,
            "gre_verbal": 150,
            "college": "能源与动力学院",
            "recommendation": "<Recommendation 3>",
            "student_id": null,
            "research": "<Research 5>",
            "name": null,
            "project": "<Project 4>",
            "language_reading": 20,
            "language_listening": 20,
            "language_speaking": 20,
            "email": "lixuanqi1995@gmail.com",
            "language_type": "TOEFL"
        },
        {
            ...
        }
    ]
}
```

##### POST

###### from-data

###### response

#### /applicants/<applicant_id>

#### /tokens

#### /users

#### /search/applications

#### /recommendations

##### GET

###### response

```json
{
    "recommendations": [
        {
            "id": 1,
            "name": "无推荐信",
            "value": 1
        },
        {
          	...
        }
    ]
}
```

#### /researches

##### GET

###### response

``` json
{
    "researches": [
        {
            "id": 1,
            "name": "无科研经历",
            "value": 1
        },
        {
        	...
        }
    ]
}
```



#### /projects

##### GET

###### response

```json
{
    "projects": [
        {
            "id": 1,
            "name": "无相关实习经历，有个人项目",
            "value": 2
        },
        {
            ...
        }
    ]
}
```



#### /tags 

##### GET

###### response

```json
{
    "tags": [
        {
            "id": 1,
            "name": "渣三维"
        },
        {
            ...
        }
    ]
}
```

#### /countries

##### GET

###### response

```json
{
    "countries": [
        {
            "id": 3,
            "name": "加拿大"
        },
        {
           	...
        }
    ]
}
```

