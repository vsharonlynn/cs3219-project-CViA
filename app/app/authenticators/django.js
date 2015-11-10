import Base from 'ember-simple-auth/authenticators/base';

export default Base.extend({
  restore(data) {
    return new Ember.RSVP.Promise(function(resolve, reject) {
        if(Ember.isEmpty(data)) {
            reject();
        }
        Ember.$.ajax({
            url: 'http://localhost:8000/api/users/current/',
            type: 'GET',
            headers: {
              "Authorization": "Token " + data.key
            }
        }).then(function(responseObject) {
            resolve(Object.assign(responseObject, { key: data.key }));
        }, function(jqXHR) {
            reject(jqXHR);
        });
    });
  },

  authenticate(options) {
    return new Ember.RSVP.Promise(function(resolve, reject) {
         Ember.$.ajax({
             url: 'http://localhost:8000/rest-auth/login/',
             type: 'POST',
             data: options,
             dataType: 'json'
         }).then(function(responseObject) {
             Ember.run(function() { resolve(responseObject); });
         }, function(jqXHR) {
             Ember.run(function() { reject(jqXHR); });
         });
     });
  },

  invalidate(data) {
    return new Ember.RSVP.Promise(function(resolve, reject) {
         Ember.$.ajax({
             url: 'http://localhost:8000/rest-auth/logout/',
             type: 'POST'
         }).then(function(responseObject) {
             Ember.run(function() { resolve(responseObject); });
         }, function(jqXHR) {
             Ember.run(function() { reject(jqXHR); });
         });
     });
  }
});
