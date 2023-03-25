$(function() {
    document.querySelector("button.expand").addEventListener(
        "click",
        function (e) {
            e.preventDefault();
            const button = e.currentTarget;
            const txtarea = document.querySelector("#input");
            button.classList.add("loading");
            button.disabled = true;
            // setTimeout(() => {
            //     button.classList.add("loaded");
            //     setTimeout(() => {
            //         button.classList.add("finished");
            //         setTimeout(() => {
            //             button.classList.remove("finished");
            //             button.classList.remove("loaded");
            //             button.classList.remove("loading");
            //             button.disabled = false;
            //         }, 1500);
            //     }, 700);
            // }, 1500);
            getResponse().then(function(data) {
                setTimeout(() => {
                    button.classList.add("loaded");
                    setTimeout(() => {
                        button.classList.add("finished");
                        setTimeout(() => {
                            button.classList.remove("finished");
                            button.classList.remove("loaded");
                            button.classList.remove("loading");
                            button.disabled = false;
                        }, 1500);
                    }, 700);
                }, 1500);
                $('#response').html(data);
            }).catch(function(err) {
                console.log(err)
            })
        }
    );
});

function getResponse() {
    return new Promise(function(resolve, reject) {
        $.ajax({
            type:'POST',
            url:'',
            data:{
                input:$('#input').val(),
                csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val(),
            },
            success: function(data){
                resolve(data)
            },
            error: function(err) {
                reject
            }
        });
    });
}