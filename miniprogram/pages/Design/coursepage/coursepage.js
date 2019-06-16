// pages/coursepage/coursepage.js
Page({
  data: {
    classId: 1936,
    classTitle: '单课标题示例',
    classContent: '课程内容 关于本节课必要的文字说明',
    classWorks: '作业描述 如作业要求等具体要求',
    classEndTime: '2020-02-23',
    classVideoUrl: 'http://wxsnsdy.tc.qq.com/105/20210/snsdyvideodownload?filekey=30280201010421301f0201690402534804102ca905ce620b1241b726bc41dcff44e00204012882540400&bizid=1023&hy=SH&fileparam=302c020101042530230204136ffd93020457e3c4ff02024ef202031e8d7f02030f42400204045a320a0201000400',
    worksSub: ['1）	在故事里，袋鼠妈妈提出许多选择，让贝普可以成为“风”、“鸟”、“蜥蜴”等，用自己的话说一说，为什么贝普不想成为它们呢？那么贝普想成为“谁”呢？','2）	对于贝普来说，妈妈的心跳就代表“妈妈的爱”——温暖、亲切、带给他安全感。你觉得还有什么可以代表“妈妈的爱”呢？请说出来或者画出来吧。'],//客观题 图片

  },

  onLoad : function (e) {
    console.log(e.class_id);
    var that = this;
    wx.request({
      url: 'http://127.0.0.1:5000/funid3',
      method: "GET",
      data: {
       
      },
      header: { 'Content_Type': 'application/x-www-form-urlencoded' },
      success: function (res) {
        // that.setData({
        //   courseId: res.data.courseId,
        //   classId: res.data.classId,
        //   classTitle: res.data.classTitle,
        //   classContent: res.data.classContent,
        //   classWorks: res.data.classWorks,
        //   classEndTime: res.data.classEndTime,
        //   classVideoUrl: res.data.classVideoUrl,
        //   worksSub: res.data.worksSub,//客观题 图片
        // })
      }
    })
  },
  // 上传图片
  doUpload: function () {
    // 选择图片
    wx.chooseImage({
      count: 1,
      sizeType: ['compressed'],
      sourceType: ['album', 'camera'],
      success: function (res) {

        wx.showLoading({
          title: '上传中',
        })

        const filePath = res.tempFilePaths[0]

        // 上传图片
        const cloudPath = 'my-image' + filePath.match(/\.[^.]+?$/)[0]
        wx.cloud.uploadFile({
          cloudPath,
          filePath,
          success: res => {
            console.log('[上传文件] 成功：', res)

            app.globalData.fileID = res.fileID
            app.globalData.cloudPath = cloudPath
            app.globalData.imagePath = filePath

            wx.navigateTo({
              url: '../storageConsole/storageConsole'
            })
          },
          fail: e => {
            console.error('[上传文件] 失败：', e)
            wx.showToast({
              icon: 'none',
              title: '上传失败',
            })
          },
          complete: () => {
            wx.hideLoading()
          }
        })

      },
      fail: e => {
        console.error(e)
      }
    })
  },
})