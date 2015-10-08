${h.form('post', action=i18n_url('auth:login'))}
    % if form.error:
    ${form.error}
    % endif

    ${csrf_tag()}
    <input type="hidden" name="next" value="${next_path}">
    <p>
        ${form.username.label}
        ${form.username}
        % if form.username.error:
        ${form.username.error}
        % endif
    </p>
    <p>
        ${form.password.label}
        ${form.password}
        % if form.password.error:
        ${form.password.error}
        % endif
    </p>
    <p class="buttons">
        <button type="submit" class="primary"><span class="icon"></span> ${_('Login')}</button>
    </p>
    <p class="buttons">
    <a href="${i18n_url('auth:reset_form')}?${h.set_qparam(next=next_path)}">${_('Reset your password')}</a>
    </p>
</form>
