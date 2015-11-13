import { moduleForComponent, test } from 'ember-qunit';
import hbs from 'htmlbars-inline-precompile';

moduleForComponent('cvia-signup-form', 'Integration | Component | cvia signup form', {
  integration: true
});

test('it renders', function(assert) {
  assert.expect(2);

  // Set any properties with this.set('myProperty', 'value');
  // Handle any actions with this.on('myAction', function(val) { ... });

  this.render(hbs`{{cvia-signup-form}}`);

  assert.equal(this.$().text().trim(), '');

  // Template block usage:
  this.render(hbs`
    {{#cvia-signup-form}}
      template block text
    {{/cvia-signup-form}}
  `);

  assert.equal(this.$().text().trim(), 'template block text');
});
