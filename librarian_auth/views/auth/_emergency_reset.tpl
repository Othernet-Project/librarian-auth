<%namespace name="forms" file="/ui/forms.tpl"/>

${h.form('post', action=i18n_url('emergency:reset'))}
    ${forms.form_errors([form.error]) if form.error else ''}
    ${csrf_tag()}
    ${forms.field(form.emergency_reset)}
    ## Translators, help text displayed below emergency reset token field
    ${forms.field_help(_('Please contact Outernet to obtain your emergency reset token.'))}
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
    <p class="buttons">
        ## Translators, used as label for button that performs emergency reset
        <button type="submit" class="primary"><span class="icon"></span> ${_('Reset')}</button>
    </p>
</form>
