<%inherit file='base.tpl'/>
<%namespace name='emergency_reset_form' file='_emergency_reset.tpl'/>

## Translators, used as page title
<%block name="title">${_('Emergency reset')}</%block>

<div class="h-bar">
    ## Translators, used as page heading
    <h2>${_('Perform emergency reset')}</h2>
</div>

<div class="full-page-form">
    ${emergency_reset_form.body()}
</div>


