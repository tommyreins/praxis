function onSuccess(googleUser) {
  var profile = googleUser.getBasicProfile();
  console.log('ID: ' + profile.getId()); // Do not send to your backend! Use an ID token instead.
  console.log('Name: ' + profile.getName());
  console.log('Image URL: ' + profile.getImageUrl());
  console.log('Email: ' + profile.getEmail()); // This is null if the 'email' scope is not present.
  window.setTimeout(function(){
    // Move to a new location or you can do something else
    location.href = "create.html";
    }, 5000);
  
}
function onFailure(error) {
  console.log(error);
}
function renderButton() {
  gapi.signin2.render('my-signin2', {
    'scope': 'profile email',
    'width': 240,
    'height': 50,
    'longtitle': true,
    'theme': 'dark',
    'onsuccess': onSuccess,
    'onfailure': onFailure
  });
}
function Init() {
  console.log('Init...');
  gapi.load('auth2', function() {
    gapi.auth2.init();
  });
}
function signMeOut() {
  console.log('Signing out...');
  var auth2 = gapi.auth2.getAuthInstance();
  auth2.signOut().then(function () {
    console.log('User signed out.');
  });
}