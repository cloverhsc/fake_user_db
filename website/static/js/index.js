$(document).ready(function(){
    // get csrf token for send post request
   function getCookie(name)
   {
       var cookieValue = null;
       if (document.cookie && document.cookie != '')
       {
           var cookies = document.cookie.split(';');
           for (var i = 0; i < cookies.length; i++)
           {
               var cookie = jQuery.trim(cookies[i]);
               // Does this cookie string begin with the name we want?
               if (cookie.substring(0, name.length + 1) == (name + '='))
               {
                   cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                   break;
               }
           }
       }
       return cookieValue;
   }
   var csrftoken = getCookie('csrftoken');

    $.ajax({
        beforeSend: function(xhr, settings){
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        },
        type: "POST",
        url: "api/userlist/",
        dataType: "json",
        data: "",
        success:function(msg){
            console.log(msg);
        },
        error:function(xhr, textStatus, errorThrown) {
            alert("Please report this error: "+errorThrown+xhr.status+xhr.responseText);
        }
    });     // end of ajax

});    // end of ready
