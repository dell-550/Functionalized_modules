package model

type V struct {
	Userid      int    `:"userid"`      // 用户id
	Username    string `:"username"`    // 用户名
	Title       string `:"title"`       // 帖子标题
	Id          int    `:"id"`          // 帖子id
	Picturepath string `:"picturepath"` // 图片路径
}

type V_post_user20 struct {
	Id            int    `:"id"`            // 帖子id
	Title         string `:"title"`         // 帖子标题
	Description   string `:"description"`   // 帖子内容
	OwnerId       int    `:"owner_id"`      // 发帖人id
	Username      string `:"username"`      // 作者名
	Time          string `:"time"`          // 发帖时间
	LikeNumbers   int    `:"LikeNumbers"`   // 点赞数
	ReviewNumbers int    `:"reviewNumbers"` // 评论数
	Picturepath   string `:"picturepath"`   // 图片路径
	Type          string `:"type"`          // 帖子分区
	Collect       int    `:"collect"`       // 收藏数
}

type Notes struct {
	Id       int    `:"id"`
	Content  string `:"content"`
	ReaderId int    `:"reader_id"`
	WriteId  int    `:"write_id"`
}

type Postings struct {
	Id            int    `:"id"`            // 帖子id
	Title         string `:"title"`         // 帖子标题
	Description   string `:"description"`   // 帖子内容
	OwnerId       int    `:"owner_id"`      // 发帖人id
	Username      string `:"username"`      // 作者名
	Time          string `:"time"`          // 发帖时间
	LikeNumbers   int    `:"LikeNumbers"`   // 点赞数
	ReviewNumbers int    `:"reviewNumbers"` // 评论数
	Picturepath   string `:"picturepath"`   // 图片路径
	Type          string `:"type"`          // 帖子分区
	Collect       int    `:"collect"`       // 收藏数
}

type Reviews struct {
	Id       int    `:"id"`       // 评论id
	Contents string `:"contents"` // 评论内容
	Time     string `:"time"`     // 评论时间
	PostId   int    `:"post_id"`  // 帖子id
	UserId   int    `:"user_id"`  // 评论人id
}

type Type struct {
	Id       int    `:"id"`
	PostType string `:"post_type"` // 帖子类型
}

type User struct {
	Userid    int    `:"userid"`    // 用户id
	Username  string `:"username"`  // 用户名
	Useremail string `:"useremail"` // 用户邮箱
	Password  string `:"password"`  // 密码
	Picture   string `:"picture"`   // 用户头像路径
	Time      string `:"time"`      // 注册时间
	Disable   string `:"disable"`   // 用户属性
	Content   string `:"content"`   // 个人签名
}
