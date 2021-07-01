import socket

so = socket.socket()
so.bind(('127.0.0.1', 9560))
so.listen(5)
conn, addr = so.accept()

request_data = conn.recv(1024).decode('utf8')
print(request_data)

data_list = request_data.split('\r\n')
print(data_list)
link_data = dict()
for item in data_list:
    if ':' in item:
        print(item.split(':', 1))
        key, value = item.split(':', 1)
        link_data[key.strip()] = value.strip()
print(link_data)
magic_string = '258EAFA5-E914-47DA-95CA-C5AB0DC85B11'
value = link_data.get('Sec-WebSocket-Key')+magic_string
import base64,hashlib
print(value,len(value))
print(hashlib.sha1(value.encode('utf8')).digest(),len(hashlib.sha1(value.encode('utf8')).digest()))
ac = base64.b64encode(hashlib.sha1(value.encode('utf8')).digest())
print(ac)
response_temp = "HTTP/1.1 101 Switching Protocols\r\n" \
               "Upgrade:websocket\r\n" \
               "Connection: Upgrade\r\n" \
               "Sec-WebSocket-Accept: %s\r\n" \
               "WebSocket-Location: ws://127.0.0.1:9560/ws\r\n\r\n"
response_str = response_temp%(ac.decode('utf8'))
conn.send(response_str.encode('utf8'))
print(response_str.encode('utf8'))

while True:
    hash_str = conn.recv(1024)
    print(hash_str)
    # hash_str = b'\x81\xe5\x95\x8a\xe5\xae\x9e\xe6\x89\x93\xe5\xae\x9e\xe7\x9a\x84\xe9\x98\xbf\xe8\xbe\xbe\xe7\x8e\xb0\xe9\x87\x91\xe9\x98\xbf\xe8\x90\xa8\xe7\x9a\x84\xe7\xbb\xbf\xe5\x8d\xa1\xe5\x86\xb3\xe5\xae\x9a\xe4\xba\x86\xe5\x8d\xa1\xe5\xbe\xb7\xe5\x8a\xa0\xe6\x8b\x89\xe5\xbc\x80\xe8\xb7\x9d\xe7\xa6\xbb\xe5\xa4\xa7\xe9\x87\x8f'
    # msg = b'\x81\xfe\xb8tD\xa4^\xfc\xd5B+\xf9'
    hash_num = hash_str[1] & 127
    print(hash_str[1], hash_str)
    if hash_num == 127:
        extend_payload_len = hash_str[2:10]
        mask = hash_str[10:14]
        decoded = hash_str[14:]
    if hash_num == 126:
        extend_payload_len = hash_str[2:4]
        mask = hash_str[4:8]
        decoded = hash_str[8:]
    if hash_num <= 125:
        extend_payload_len = None
        mask = hash_str[2:6]
        decoded = hash_str[6:]
    str_byte = bytearray()
    for i in range(len(decoded)):
        byte = decoded[i] ^ mask[i % 4]
        str_byte.append(byte)
    print(str_byte.decode('utf8'))
    conn.send(b'\x81Rasd \xe5\x95\x8a\xe5\xae\x9e\xe6\x89\x93\xe5\xae\x9e\xe7\x9a\x84\xe9\x98\xbf\xe8\xbe\xbe\xe7\x8e\xb0\xe9\x87\x91\xe9\x98\xbf\xe8\x90\xa8\xe7\x9a\x84\xe7\xbb\xbf\xe5\x8d\xa1\xe5\x86\xb3\xe5\xae\x9a\xe4\xba\x86\xe5\x8d\xa1\xe5\xbe\xb7\xe5\x8a\xa0\xe6\x8b\x89\xe5\xbc\x80\xe8\xb7\x9d\xe7\xa6\xbb\xe5\xa4\xa7\xe9\x87\x8f')



# b'\x81\x86\xb8tD\xa4^\xfc\xd5B+\xf9'
# b'\x81\x86\x85\xcb@Z`F\xe7\xbc"v'
# b'\x81\x8c\xd9B\x1e\x0c<\xe7\xa8\xe9|\xf4\xfa\xb4s\xab\x8a\xa8'
# b'\x81\x8cB\xee\x8a5\xabn6\xdc\xc2Rb\x80\xd4\x06?\xa3'


# import struct
# msg_bytes = "hello".encode("utf8")
# token = b"\x81"
# length = len(msg_bytes)
# if length < 126:
#     token += struct.pack("B", length)
# elif length == 126:
#     token += struct.pack("!BH", 126, length)
# else:
#     token += struct.pack("!BQ", 127, length)
# msg = token + msg_bytes
# print(msg)






'''
b'GET / HTTP/1.1\r\n
Host: 127.0.0.1:9560\r\n
Connection: keep-alive\r\n
Cache-Control: max-age=0\r\n
Upgrade-Insecure-Requests: 1\r\n
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36\r\n
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9\r\n
Sec-Fetch-Site: none\r\n
Sec-Fetch-Mode: navigate\r\n
Sec-Fetch-User: ?1\r\n
Sec-Fetch-Dest: document\r\n
Accept-Encoding: gzip, deflate, br\r\n
Accept-Language: zh-CN,zh;q=0.9\r\n
Cookie: session=cbecf95c-dd69-4813-8198-20115a50ecf6\r\n\r\n'
'''
