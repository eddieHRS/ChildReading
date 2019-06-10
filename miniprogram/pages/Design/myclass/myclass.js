// pages/Design/myclass/myclass.js
Page({

  data: {
    //已选课程
    course_list:[
      {
        pageImgUrls:
          'https://i.loli.net/2019/02/08/5c5d63058df87.png',
        courseTitle: '标题从数据库获取1',
        courseProgress: '(课程进度从数据库获取)当前进度：第n课/单课课名',
        courseLinks: '#',
      },
    ],
  },

  onLoad: function (options) {
    //交互
    var that = this
    wx.request({
      url: 'http://127.0.0.1:5000/myclass',
      method: "POST",
      data: {
        stu_id:'1016001'
      },
      header: { 'Content_Type': 'application/x-www-form-urlencoded' },
      success: function (res) {
        that.setData({
          courseList: res.data.course_list
        })
      }
    })
  },

  onReady: function () {

  },

  onShow: function () {

  },


  goToCoursePage: function () {
    wx.navigateTo({
      url: '../coursepage/coursepage'
    });
  },
})