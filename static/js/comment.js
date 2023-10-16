// 使用JavaScript来请求评论数据
// 可以使用AJAX、fetch等方法发送请求
function fetchComments() {
    fetch('/get_commentsTest')
        .then(response => response.json())
        .then(data => {
            // 在页面上动态显示评论
            const ar = data.data // 获取二维元组数据
            const n = data.num
            console.log(ar)
            const commentsDiv = document.getElementById('comments');
            for (var i = 0; i < n; i++) {

                const commentElement = document.createElement('div');
                commentElement.textContent = ar[i][1] + ":  " + ar[i][3];
                commentsDiv.appendChild(commentElement);

            }
        });
}

// 在页面加载时请求评论数据
window.onload = fetchComments;