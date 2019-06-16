// pages/department/department.js
var titleList = [
  '3-6 岁', '7-9 岁', '10-12 岁', '动物朋友', '探险奇遇', '成长故事'
]
Page({
  data: {
  },
  onLoad:function (e) {
    var that = this
    var type = e.type;
    wx.request({
      url: 'http://127.0.0.1:5000/funid0',
      method: "GET",
      data: {
        'type' : type,
      },
      header: {'Content_Type' : 'application/x-www-form-urlencoded'},
      success : function(res) {
        console.log(res.data.data)
        that.setData({
          lst : res.data.data
        })
      }
    })
  },
  onShow: function() {
    var that = this
  },

  goToCourseGuide: function (e) {
    var course_id = e.currentTarget.dataset.course_id;
    console.log("course_id" + course_id)
    wx.navigateTo({
      url: '../course/course?course_id='+course_id
    });
  }
})