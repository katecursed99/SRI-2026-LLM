def FilterOutputs(reply, priv_key, filt_mode):
    if filt_mode:
        reply.replace(priv_key, "[REDACTED SECRET KEY]")