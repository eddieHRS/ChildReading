// pages/Design/myclass/myclass.js
var app = getApp();
Page({

  data: {
    //已选课程
    classList:[
      {
        // pageImgUrls: 'https://i.loli.net/2019/02/08/5c5d63058df87.png',
        name: '班级名字',
        stage: '当前的进度',
        class_id: 'c001'
      }
    ],
    pcourseList:[
      {
        pcourse_id: '',
        name:'单课的名字'
      }
    ]
  },

  onLoad: function () {
    //交互

  },

  onReady: function () {

  },

  onShow: function () {
    var that = this
    wx.request({
      url: 'http://127.0.0.1:5000/myclass',
      method: "GET",
      data: {
        stu_id: app.globalData.openid
      },
      success: function (res) {
        console.log(res.data.data.classList)
        console.log(app.globalData.openid)
        console.log(res.data.data.pcourseList)
        that.setData({
          classList: res.data.data.classList,
          pcourseList: res.data.data.pcourseList
        })
      },

    })
  },


  goToCoursePage: function (e) {
    var type = e.currentTarget.dataset.type;
    var url = '../coursepage/coursepage?type='+type;
    //type标记单课还是套课 1 是单课 ， 2是套课
    if(type == 1){
      url = url + "&id=" + e.currentTarget.dataset.pcourse_id
    }
    else{
      url = url + "&id=" + e.currentTarget.dataset.class_id;
    }
    console.log(url)
    wx.navigateTo({
      url: url
    });
  },
  
  delpercourse: function(e){
    var that = this;
    console.log(e.currentTarget.dataset.pcourse_id)
    wx.request({
      url: 'http://127.0.0.1:5000/delpercourse',
      data: {
        'stu_id': app.globalData.openid,
        'pcourse_id': e.currentTarget.dataset.pcourse_id
      },
      success: function(res){
        console.log(res)
        wx.showToast({
          title: '退课成功',
          icon: 'success',
          duration: 2000//持续的时间
        })
        that.onShow()
      }
    })
  },

  delsetcourse: function(e){
    var that = this;
    console.log(e.currentTarget.dataset.class_id)
    wx.request({
      url: 'http://127.0.0.1:5000/delsetcourse',
      data: {
        'stu_id': app.globalData.openid,
        'class_id': e.currentTarget.dataset.class_id
      },
      success: function (res) {
        console.log(res)
        wx.showToast({
          title: '退课成功',
          icon: 'success',
          duration: 2000//持续的时间
        })
        that.onShow()
      }
    })
  } 
})