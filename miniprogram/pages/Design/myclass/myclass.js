// pages/Design/myclass/myclass.js
var app = getApp();
Page({

  data: {
    //已选课程
    courseList:[
      {
        pageImgUrls: 'https://i.loli.net/2019/02/08/5c5d63058df87.png',
        name: '班级名字',
        stage: '当前的进度',
        class_id: 'c001'
      }
    ],
  },

  onLoad: function (options) {
    //交互
    var that = this
    wx.request({
      url: 'http://127.0.0.1:5000/myclass',
      method: "GET",
      data: {
        stu_id: app.globalData.openid
      },
      success: function (res) {
        console.log(res.data.data)
        that.setData({
          courseList: res.data.data
        })
      }
    })
  },

  onReady: function () {

  },

  onShow: function () {

  },


  goToCoursePage: function (e) {
    var class_id = e.currentTarget.dataset.class_id;
    console.log(class_id)
    wx.navigateTo({
      url: '../coursepage/coursepage?class_id='+class_id
    });
  },
})