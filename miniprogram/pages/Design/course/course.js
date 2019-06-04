// pages/course/course.js
Page({
  data: {
    courseId: 20190223,
    courseTitle: '标题示例',
    coursePrice: 0,
    time:'2019-02-23',
    courseContent: '这是一段课程内容简介',
    teacherIntro: '这是一段教师简介'
  },
  onLoad : function(e) {
    var that = this
    var course_id = e.course_id;
    console.log(course_id);
    wx.request({
      url: 'http://127.0.0.1:5000/funid2',
      method : "GET",
      data : {
        'course_id': course_id
      },
      header: { 'Content_Type': 'application/x-www-form-urlencoded' },
      success : function(res)  {
        wx.setNavigationBarTitle({
          title: '课程',
        })
        that.setData({
          courseId: res.data.data.courseId,
          courseTitle: res.data.data.courseTitle,
          coursePrice: res.data.data.coursePrice,
          time: res.data.data.time,
          courseContent: res.data.data.courseContent,
          teacherIntro: res.data.data.teacherIntro
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