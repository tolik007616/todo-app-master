function task_append(id, name){
return "<li class=\"task task"+id+"\"> \
            <input type=\"checkbox\" class = \"done\" name=\"done\" task-id=\""+id+"\"><span class=\"task_id"+id+"\"> "+name+"</span> \
            <ul class=\"tools\"> \
            <div class=\"priority\">\
            <li class=\"up\">\
              <img src=\"static/img/arrow.png\" class=\"priority prup\" task_id=\""+id+"\" alt=\"up\">\
            </li>\
            <li class=\"down\">\
              <img src=\"static/img/arrow.png\" class=\"priority prdown\" task_id=\""+id+"\" alt=\"down\">\
            </li>\
            </div>\
            <li class=\"edt\"><img src=\"static/img/edit.png\" class=\"edit taskedit\" task_id=\""+id+"\" alt=\"edit\"></li> \
            <li class = \"trsh\"><img src=\"static/img/trash.png\" class=\"trash taskdelete\" task_id=\""+id+"\" alt=\"trash\"></li> \
            </ul> </li>"
      }

function list_append(id){
  return "<section class = \"project project_id"+id+"\">\
    <div class=\"container\">\
    \
  <div class=\"project_title\">\
        <img src=\"static/img/project.png\" alt=\"project\" class=\"logo\">\
        <span class=\"title list_id"+id+"\">New Project</span>\
        <ul class=\"tools\">\
          <li class = \"edt\"><img src=\"static/img/edit.png\" class=\"edit listedit\" alt=\"edit\" list_id =\""+id+"\"></li>\
          <li class = \"trsh\"><img src=\"static/img/trash.png\" class=\"trash listdelete\" list_id =\""+id+"\" alt=\"trash\"></li>\
        </ul>\
      </div>\
      \
      <div class=\"new_task clearfix\">\
          <img src=\"static/img/add.png\" class=\"add_img\" alt=\"add\">\
          \
          <input type=\"text\" placeholder=\"Start typing to create a task...\" id=\"type_task\" name=\"tdlist"+id+"\">\
\
          <input type=\"button\" value=\"Add Task\" class = \"add_task\" list_id =\""+id+"\">\
        \
      </div> \
      <ul class=\"tasks\" id=\"ul"+id+"\">\
      </ul>\
      </div>\
  </section>"
}

function getCookie(c_name){
    if (document.cookie.length > 0)
    {
        c_start = document.cookie.indexOf(c_name + "=");
        if (c_start != -1)
        {
            c_start = c_start + c_name.length + 1;
            c_end = document.cookie.indexOf(";", c_start);
            if (c_end == -1) c_end = document.cookie.length;
            return unescape(document.cookie.substring(c_start,c_end));
        }
    }
    return "";
 }

function change_status() {
  $('.projects').on("click", 'input[type="checkbox"]', function(event) {
  var box = $(this);
  var myurl = "/change_status/";
  id = box.attr('task-id')
  $.ajax({
   type: 'POST',
   async: true,
   dataType: 'json',
   url: myurl,
   data: {
    "id": id,
    csrfmiddlewaretoken : getCookie("csrftoken")
   },
   
   success: function (data, status, xhr) {
      
      task = $('.task'+id+' span').text()
      if (box.prop('checked')){
      $('.task'+id+' span').css("text-decoration", "line-through")}
      else{
        $('.task'+id+' span').css("text-decoration", "none")
      }
      
    
   }
  });
 });
}

function add_task() {
 $('.projects').on("click", ".new_task input[type='button']", function(event) {
  var btn = $(this);
  var list_id = btn.attr('list_id');  
  var myurl = "/add_task/";
  var inputfield = $("[name=tdlist"+list_id+"]")
  var task = inputfield.val();
  inputfield.val('');
  $.ajax({
   type: 'POST',
   async: true,
   dataType: 'json',
   url: myurl,
   data: {
    "id": list_id,
    "newtask":task,
    csrfmiddlewaretoken : getCookie("csrftoken")
   },
   
   success: function (data, status, xhr) {
        
      $('#ul'+ list_id).prepend(task_append(data['id'], data['name']))

   }
  });
 });
}

function delete_task() {
 $('.projects').on("click", ".taskdelete", function(event) {
  var btn = $(this);
  var task_id = btn.attr('task_id');  
  var myurl = "/delete_task/";  
  $.ajax({
   type: 'POST',
   async: true,
   dataType: 'json',
   url: myurl,
   data: {
    "id": task_id,    
    csrfmiddlewaretoken : getCookie("csrftoken")
   },
   
   success: function (data, status, xhr) {

    $(".task"+task_id).remove();
        
   }
  });
 });
}

function delete_list() {
 $('.projects').on("click", ".listdelete", function(event) {
  if (confirm("Delete project?")){
  var btn = $(this);
  var list_id = btn.attr('list_id');  
  var myurl = "/delete_list/";  
  $.ajax({
   type: 'POST',
   async: true,
   dataType: 'json',
   url: myurl,
   data: {
    "id": list_id,    
    csrfmiddlewaretoken : getCookie("csrftoken")
   },
   
   success: function (data, status, xhr) {
      $(".project_id"+list_id).remove();    
   }
  });
}
 });
}

function edit_list() {
 $('.projects').on("click", ".listedit", function(event) {
  var btn = $(this);
  var list_id = btn.attr('list_id');
  prevname = $('span.list_id'+list_id).text()
  if (newname = prompt("Rename project:", prevname)){    
  var myurl = "/edit_list/";  
  $.ajax({
   type: 'POST',
   async: true,
   dataType: 'json',
   url: myurl,
   data: {
    "id": list_id, 
    "newname": newname,
    csrfmiddlewaretoken : getCookie("csrftoken")
   },
   
   success: function (data, status, xhr) {
       $('span.list_id'+list_id).text(newname)   
   }
  });
}
 });
}

function edit_task() {
 $('.projects').on("click", ".taskedit", function(event) {
  var btn = $(this);
  var task_id = btn.attr('task_id');
  prevname = $('span.task_id'+task_id).text()
  if (newname = prompt("Rename task:", prevname)){    
  var myurl = "/edit_task/";  
  $.ajax({
   type: 'POST',
   async: true,
   dataType: 'json',
   url: myurl,
   data: {
    "id": task_id, 
    "newname": newname,
    csrfmiddlewaretoken : getCookie("csrftoken")
   },
   
   success: function (data, status, xhr) {
      $('span.task_id'+task_id).text(newname)   
   }
  });
}
 });
}

function add_list() {
 $('.add_list').click(function (event) {
  var btn = $(this);
  var myurl = "/add_list/";
  $.ajax({
   type: 'POST',
   async: true,
   dataType: 'json',
   url: myurl,
   data: {
    "name": "New Project",
    csrfmiddlewaretoken : getCookie("csrftoken")
   },
   
   success: function (data, status, xhr) {
    
      $('.projects').append(list_append(data['id'])) 
    
   }
  });
 });
}

function pr_up() {
 $('.projects').on("click", ".prup", function(event) {
  var btn = $(this);
  var task_id = btn.attr('task_id');  
  var myurl = "/prup/";  
  $.ajax({
   type: 'POST',
   async: true,
   dataType: 'json',
   url: myurl,
   data: {
    "id": task_id,    
    csrfmiddlewaretoken : getCookie("csrftoken")
   },
   
   success: function (data, status, xhr) {
    if (data['status']=='success'){
      $(".task"+data['swapid']).remove();
      $('.task'+task_id).after(task_append(data['swapid'], data['swapname']));
      if (data['checked']){
        $("[task-id='"+data['swapid']+"']").attr("checked","true");
      $('.task'+data['swapid']+' span').css("text-decoration", "line-through")}
      }    
   }
  });
 });
}

function pr_down() {
 $('.projects').on("click", ".prdown", function(event) {
  var btn = $(this);
  var task_id = btn.attr('task_id');  
  var myurl = "/prdown/";  
  $.ajax({
   type: 'POST',
   async: true,
   dataType: 'json',
   url: myurl,
   data: {
    "id": task_id,    
    csrfmiddlewaretoken : getCookie("csrftoken")
   },   
   success: function (data, status, xhr) {
    if (data['status']=='success'){
      $(".task"+task_id).remove();
      $('.task'+data['swapid']).after(task_append(task_id, data['name']));
      if (data['checked']){
      $("[task-id='"+task_id+"']").attr("checked","true");
      $('.task'+task_id+' span').css("text-decoration", "line-through")}
    }
  }
  });
 });
}

 $(document).ready(function(){
 change_status();
 add_task();
 delete_task();
 delete_list();
 add_list();
 edit_list();
 edit_task();
 pr_down();
 pr_up();
 });