function sendArticleComment(){
    var comment = $('#commentText').val();
    $.get('/articles/add-article-comment', {
        articleComment: comment
    }).then(res => {
        console.log(res);
    });
}