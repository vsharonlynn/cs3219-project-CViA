import DS from 'ember-data';

export default DS.Model.extend({
  title: DS.attr('string'),
  description: DS.attr('string'),
  createdAt: DS.attr('string', {
    defaultValue() {
      return new Date();
    }
  })
});
