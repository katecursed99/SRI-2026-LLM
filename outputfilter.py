def FilterOutputs(reply, priv_key, filt_mode):
    if filt_mode:
        cleaned_reply = reply.replace(priv_key, "[REDACTED SECRET KEY]")
        return cleaned_reply
    else:
        return reply