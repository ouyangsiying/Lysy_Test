{
  "actions": [
    {
      "api": "logout",
      "data": "logout"
    },
    {
      "api": "login",
      "data": "login"
    },
    {
      "api": "cashbook",
      "data": "cashbook"
    }
  ],
  "data": {
    "logout": {
      "check": 0,
      "input": {},
      "output": {}
    },
    "login": {
      "check": 0,
      "input": {
        "_token": "xxx",
        "user_name": "测试队费队长",
        "password": "111111",
        "remember": 0
      },
      "output": {}
    },
    "cashbook": {
      "check": 1,
      "input": {
          "_token": "xxx",
          "team_id":"9555",
          "type":"into",
          "user_ids":"",
          "fee":"200",
          "fee_arg":"",
          "add_date":"2018-07-20",
          "id"
          "category_id":102,
          "title":"代码记录的",
          "note":"收入的备注2",
          "into_team":""
      },
      "output": {
          "errno": 0,
          "result":{"ok"}

      }
    }
  }
}