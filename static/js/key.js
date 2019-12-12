  $('#expiration').change(function(){
    $(this).attr('value', $('#expiration').val());
});

keyinfo= function(token, description, expiration, urledu, urlsurvey){


$('#newkey').hide();
$("#token").html(token)
$("#descriptionInfo").html(description)
var date=new Date(expiration)
$("#expirationInfo").html(date.getDate()+"-"+(date.getMonth()+1)+"-"+date.getFullYear())
$("#urledu").html(urledu)
$("#urlsurvey").html(urlsurvey)

$("#keyinfo").show();
$("#addkey").show();


}

newkey= function(){
$("#keyinfo").hide();
$("#addkey").hide();
$('#newkey').show();
}

$('li.list-group-item').click(function(){
    $('li.list-group-item').removeClass("active");
    $(this).addClass("active");
});