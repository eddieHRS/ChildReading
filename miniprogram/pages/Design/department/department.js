// pages/department/department.js
var titleList = [
  '3-6 岁', '7-9 岁', '10-12 岁', '动物朋友', '探险奇遇', '成长故事'
]
Page({
  data: {
    //数据库中某类课的全部课程 n个
    lst:[
      {
        'pageImgUrls' : 'https://i.loli.net/2019/02/08/5c5d63058df87.png',
        'courseTitle' : 'course_title_1',
        'courseIntro' : 'course_intro_1',
        'courseLinks' : 'course_links_1',
        'Course_ID' : '123456'
      },
      {
        'pageImgUrls': 'https://i.loli.net/2019/02/08/5c5d63058df87.png',
        'courseTitle': 'course_title_2',
        'courseIntro': 'course_intro_2',
        'courseLinks': 'course_links_2',
        'Course_ID' : '654321'
      }
    ],
    index: 1
  },
  onLoad:function () {
    var that = this
    wx.request({
      url: '',
      method: "POST",
      data: {
        'func_id' : 0,

      },
      header: {'Content_Type' : 'application/x-www-form-urlencoded'},
      success : function(res) {
        that.setData({
          lst : res.data
        })
      }
    })
    wx.getStorage({
      key: 'jumpIndex',
      success: function (res) {
        //console.log(res)
        var i = res.data
        wx.setNavigationBarTitle({
        title: titleList[i],
        })
        that.setData({index: res.data})
      } 
    })
  },
  onShow: function() {
    var that = this
  },

  goToCourseGuide: function (e) {
    var ind = parseInt(e.currentTarget.dataset.index)
    //console.error("adsfasdfasdf" + ind)
    wx.navigateTo({
      url: '../course/course?course_upid='+this.data.lst[ind].courseId
    });
  }
})