本测试没有写前端页面，只写了后端接口，测试用postman完成
接口1：
    路由：
        127.0.0.1:8000/create
    参数：
        client：客户端(必填)
        fraction：分数(必填)
    返回数据格式：
        {
            "status": 200,
            "msg": "create success",
            "token": "f9861fef2842473a9a63a3962f42457e",
            "rank": {
                "id": 1,
                "grade": 1,
                "client": "客户端1",
                "fraction": 9999999
            }
        }
        {
            "status": 200,
            "msg": "create success",
            "token": "c80cc3845028488b9d2830a60fd698aa",
            "rank": {
                "id": 5,
                "grade": 5,
                "client": "客户端5",
                "fraction": 3453452
            }
        }
接口2：
    路由：
        127.0.0.1:8000/list/?token=xxx&start=xx&end=xx
    参数：
        token：token值(必填)
        start：排行起始值(可不填，默认为0)
        end: 排行结束值(可不填，默认为排行榜最后)
    返回数据格式：
    客户端5请求，不传start和end
    127.0.0.1:8000/list/?token=c80cc3845028488b9d2830a60fd698aa
    {
        "msg": "ok",
        "status": 200,
        "ranks": [
            {
                "id": 1,
                "grade": 1,
                "client": "客户端1",
                "fraction": 9999999
            },
            {
                "id": 2,
                "grade": 2,
                "client": "客户端2",
                "fraction": 9500112
            },
            {
                "id": 3,
                "grade": 3,
                "client": "客户端3",
                "fraction": 9233333
            },
            {
                "id": 4,
                "grade": 4,
                "client": "客户端4",
                "fraction": 5445444
            },
            {
                "id": 5,
                "grade": 5,
                "client": "客户端5",
                "fraction": 3453452
            },
            {
                "id": 6,
                "grade": 6,
                "client": "客户端6",
                "fraction": 2342342
            },
            {
                "id": 7,
                "grade": 7,
                "client": "客户端7",
                "fraction": 66666
            },
            {
                "id": 8,
                "grade": 8,
                "client": "客户端8",
                "fraction": 66666
            }
        ],
        "rank": {
            "id": 5,
            "grade": 5,
            "client": "客户端5",
            "fraction": 3453452
        }
    }
    再添加两条数据后，客户端10请求，查排行榜3-6的
    127.0.0.1:8000/list/?token=ba2e71f428fa475990752bab416d506b&start=3&end=6
    {
    "msg": "ok",
    "status": 200,
    "ranks": [
        {
            "id": 3,
            "grade": 3,
            "client": "客户端3",
            "fraction": 9233333
        },
        {
            "id": 4,
            "grade": 4,
            "client": "客户端4",
            "fraction": 5445444
        },
        {
            "id": 5,
            "grade": 5,
            "client": "客户端5",
            "fraction": 3453452
        },
        {
            "id": 6,
            "grade": 6,
            "client": "客户端6",
            "fraction": 2342342
        }
    ],
    "rank": {
        "id": 10,
        "grade": 10,
        "client": "客户端10",
        "fraction": 75
    }
}


