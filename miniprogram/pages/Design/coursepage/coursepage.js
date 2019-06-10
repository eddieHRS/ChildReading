// pages/coursepage/coursepage.js
Page({
  data: {
    courseId: 20190223,
    classId: 1936,
    classTitle: '标题示例',
    classContent: '课程内容 关于本节课必要的文字说明',
    classWorks: '作业描述 如作业要求等具体要求',
    classEndTime: '2020-02-23',
    classVideoUrl: '#',
    worksSub: ['1）	在故事里，袋鼠妈妈提出许多选择，让贝普可以成为“风”、“鸟”、“蜥蜴”等，用自己的话说一说，为什么贝普不想成为它们呢？那么贝普想成为“谁”呢？','2）	对于贝普来说，妈妈的心跳就代表“妈妈的爱”——温暖、亲切、带给他安全感。你觉得还有什么可以代表“妈妈的爱”呢？请说出来或者画出来吧。'],//客观题 图片
    worksObj: ['',...''],//主观题 选项结果

  },

  onLoad : function (e) {
    var that = this;
    wx.request({
      url: 'http://127.0.0.1:5000/funid3',
      method: "GET",
      data: {
        'func_id': 3
      },
      header: { 'Content_Type': 'application/x-www-form-urlencoded' },
      success: function (res) {
        that.setData({
          courseId: res.data.courseId,
          classId: res.data.classId,
          classTitle: res.data.classTitle,
          classContent: res.data.classContent,
          classWorks: res.data.classWorks,
          classEndTime: res.data.classEndTime,
          classVideoUrl: res.data.classVideoUrl,
          worksSub: res.data.worksSub,//客观题 图片
          worksObj: res.data.worksObj//主观题 选项结果
        })
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