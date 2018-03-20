from gmail import GMail, Message
from random import choice
gmail = GMail('Tai <alohapham39@gmail.com>', 'taichimto123')
template = '''
<h2 style="text-align: center;">Đơn xin nghỉ học&nbsp;</h2>
<p>Em chảo thầy</p>
<p>T&ecirc;n em l&agrave; <span style="color: #ff99cc;">Phạm Ph&uacute; T&agrave;i</span></p>
<p>H&ocirc;m nay {{ẩy chỉa}} em bị ẩy chỉa n&ecirc;n em xin thầy cho em nghỉ 1 buổi&nbsp;<img src="http://htmleditor.tools/tinymce465/plugins/emoticons/img/smiley-yell.gif" alt="yell" /></p>
<p>T&agrave;i Phạm</p>
'''
reasons = ['đau bụng', 'lang ben', 'ebola']
reason = choice(reasons)
content = template.replace('{{ẩy chỉa}}',reason)

msg = Message('Tai', to = 'Techkidsc4e16@gmail.com', html = content)
gmail.send(msg)
