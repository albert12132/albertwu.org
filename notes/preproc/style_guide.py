def run(text):
    return text.replace('<N>', '<span class="non-ess">N</span>').replace('<P>', '<span class="python">P</span>')
