import DS from 'ember-data';

export default DS.Model.extend({
  title: DS.attr('string'),
  description: DS.attr('string'),
  author: DS.belongsTo('user'),
  raw: DS.belongsTo('upload'),

  ago: Ember.computed('createdAt', function() {
    return moment(this.get('createdAt')).add(8, 'hours').fromNow();
  }),

  createdAt: DS.attr('string', {
    defaultValue() {
      return new Date();
    }
  })
});
