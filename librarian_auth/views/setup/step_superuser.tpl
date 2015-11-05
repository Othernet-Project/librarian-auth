<%inherit file='/setup/setup_base.tpl'/>

<%namespace name="forms" file="/ui/forms.tpl"/>

<%block name="step_title">
    <span class="icon icon-user-up"></span>
    ${_('Superuser account')}
</%block>

<%block name="step_desc">
    <p>
        ${_('The superuser account is used to maintain the library and configure the receiver.')}
    </p>
</%block>

<%block name="step">
<div class="step-superuser-form">
    % if form.error:
    ${form.error}
    % endif
    ${forms.field(form.username)}
    ${forms.field(form.password1)}
    ${forms.field(form.password2)}
    <p class="superuser-note">
        <span class="label">${_('Password reset token')}</span>
        <span class="large">${reset_token}</span>
        <span class="field-help">
            ## Translators, shown as a message under the password reset token.
            ## Password reset token is a 6-digit number that is used to reset
            ## the user password.
            ${_('Please write this password reset token down and store it securely. You will need it if you ever need to reset your password.')}
        </span>
        ${h.HIDDEN('reset_token', reset_token)}
    </p>
</div>
</%block>
