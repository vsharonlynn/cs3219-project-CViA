import { moduleForComponent, test } from 'ember-qunit';
import hbs from 'htmlbars-inline-precompile';

moduleForComponent('cvia-employee-navbar', 'Integration | Component | cvia employee navbar', {
  integration: true
});

test('it renders', function(assert) {
  assert.expect(2);

  // Set any properties with this.set('myProperty', 'value');
  // Handle any actions with this.on('myAction', function(val) { ... });

  this.render(hbs`{{cvia-employee-navbar}}`);

  assert.equal(this.$().text().trim(), '');

  // Template block usage:
  this.render(hbs`
    {{#cvia-employee-navbar}}
      template block text
    {{/cvia-employee-navbar}}
  `);

  assert.equal(this.$().text().trim(), 'template block text');
});
