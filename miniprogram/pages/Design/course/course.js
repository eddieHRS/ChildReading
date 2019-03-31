// pages/course/course.js
Page({
  data: {
    /*courseId: 20190223,
    courseTitle: '标题示例',
    coursePrice: 0,
    time:'2019-02-23',
    courseContent: '这是一段课程内容简介',
    teacherIntro: '这是一段教师简介'*/
  },
  onLoad : function(option) {
    var that = this
    wx.request({
      url: '',
      method : "POST",
      data : {"func_id" : 2, "course_id":option.course_upid},
      header: { 'Content_Type': 'application/x-www-form-urlencoded' },
      success : function(res)  {
        that.setData({
          courseId: res.data.courseId,
          courseTitle: res.data.courseTitle,
          coursePrice: res.data.coursePrice,
          time: res.data.time,
          courseContent: res.data.courseContent,
          teacherIntro: res.data.teacherIntro
        })
      }
    })
  },
  getPay: function(e) {
    //调用支付接口
  },
  getMall: function(e) {
    wx.navigateTo({
      url: '../../Others/links/links'
    });
  }
})