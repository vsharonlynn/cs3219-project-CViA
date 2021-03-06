import Ember from 'ember';
import DS from 'ember-data';

export default DS.Model.extend({
  first_name: DS.attr('string'),
  last_name: DS.attr('string'),
  role: DS.attr('string'),
  email: DS.attr('string'),
  fullName: Ember.computed('first_name', 'last_name', function() {
    return this.get('first_name') + ' ' + this.get('last_name');
  })
});
