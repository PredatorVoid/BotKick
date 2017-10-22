#Script made by PredatorVoids from LineAlpha import LineClient from LineAlpha.LineApi import LineTracer from LineAlpha.LineThrift.ttypes import Message from LineAlpha.LineThrift.TalkService import Client import time, datetime, random ,sys, re, string, os, json

reload(sys) sys.setdefaultencoding('utf-8')

client = LineClient() client._qrLogin("line://au/q/")

profile, setting, tracer = client.getProfile(), client.getSettings(), LineTracer(client) offbot, messageReq, wordsArray, waitingAnswer = [], {}, {}, {}

print client._loginresult()

wait = { 'readPoint':{}, 'readMember':{}, 'setTime':{}, 'ROM':{} }

setTime = {} setTime = wait["setTime"]

def sendMessage(to, text, contentMetadata={}, contentType=0): mes = Message() mes.to, mes.from_ = to, profile.mid mes.text = text

mes.contentType, mes.contentMetadata = contentType, contentMetadata
if to not in messageReq:
    messageReq[to] = -1
messageReq[to] += 1
client._client.sendMessage(messageReq[to], mes)
def NOTIFIED_ADD_CONTACT(op): try: sendMessage(op.param1, client.getContact(op.param1).displayName + "Thanks for add") except Exception as e: print e print ("\n\nNOTIFIED_ADD_CONTACT\n\n") return

tracer.addOpInterrupt(5,NOTIFIED_ADD_CONTACT)

def NOTIFIED_ACCEPT_GROUP_INVITATION(op): #print op try: sendMessage(op.param1, client.getContact(op.param2).displayName + "WELCOME to " + group.name) except Exception as e: print e print ("\n\nNOTIFIED_ACCEPT_GROUP_INVITATION\n\n") return

tracer.addOpInterrupt(17,NOTIFIED_ACCEPT_GROUP_INVITATION)

def NOTIFIED_KICKOUT_FROM_GROUP(op): try: sendMessage(op.param1, client.getContact(op.param3).displayName + " Mampus lo anjing") except Exception as e: print e print ("\n\nNOTIFIED_KICKOUT_FROM_GROUP\n\n") return

tracer.addOpInterrupt(19,NOTIFIED_KICKOUT_FROM_GROUP)

def NOTIFIED_LEAVE_GROUP(op): try: sendMessage(op.param1, client.getContact(op.param2).displayName + " Mampus lo anjing") except Exception as e: print e print ("\n\nNOTIFIED_LEAVE_GROUP\n\n") return

tracer.addOpInterrupt(15,NOTIFIED_LEAVE_GROUP)

def NOTIFIED_READ_MESSAGE(op): #print op try: if op.param1 in wait['readPoint']: Name = client.getContact(op.param2).displayName if Name in wait['readMember'][op.param1]: pass else: wait['readMember'][op.param1] += "\n・" + Name wait['ROM'][op.param1][op.param2] = "・" + Name else: pass except: pass

tracer.addOpInterrupt(55, NOTIFIED_READ_MESSAGE)

def RECEIVE_MESSAGE(op): msg = op.message try: if msg.contentType == 0: try: if msg.to in wait['readPoint']: if msg.from_ in wait["ROM"][msg.to]: del wait["ROM"][msg.to][msg.from_] else: pass except: pass else: pass except KeyboardInterrupt: sys.exit(0) except Exception as error: print error print ("\n\nRECEIVE_MESSAGE\n\n") return

tracer.addOpInterrupt(26, RECEIVE_MESSAGE)

def SEND_MESSAGE(op): msg = op.message try: if msg.toType == 2: if msg.contentType == 0: #if "gname:" in msg.text: #-------------------------------------------------------------- if msg.text == "Bantai": print "ok" _name = msg.text.replace("Bantai","") gs = client.getGroup(msg.to) sendMessage(msg.to,"Kick By PredatorsVoid") targets = [] for g in gs.members: if _name in g.displayName: targets.append(g.mid) if targets == []: sendMessage(msg.to,"error") else: for target in targets: try: klist=[client] kicker=random.choice(klist) kicker.kickoutFromGroup(msg.to,[target]) print (msg.to,[g.mid]) except: sendText(msg.to,"error") #------------------------------------------------------------- if msg.text == "Test": start = time.time() sendMessage(msg.to, "Speed") elapsed_time = time.time() - start sendMessage(msg.to, "%sseconds" % (elapsed_time)) #------------------------------------------------------------- if msg.text == "Spam": sendMessage(msg.to,"3") sendMessage(msg.to,"2") sendMessage(msg.to,"1") sendMessage(msg.to,"Despacito") sendMessage(msg.to,"Ay!") sendMessage(msg.to,"Fonsi!") sendMessage(msg.to,"D.Y.!") sendMessage(msg.to,"Ohhh") sendMessage(msg.to,"Oh, no, oh, no") sendMessage(msg.to,"Oh") sendMessage(msg.to,"Hey, yeah!") sendMessage(msg.to,"Diridiri dirididi Daddy") sendMessage(msg.to,"Go!") sendMessage(msg.to,"Si sabes que ya llevo un rato mirándote") sendMessage(msg.to,"Tengo que bailar contigo hoy") sendMessage(msg.to,"Vi que tu mirada ya estaba llamándome") sendMessage(msg.to,"Muéstrame el camino que yo voy, oh") sendMessage(msg.to,"Tú, tú eres el imán y yo soy el metal") sendMessage(msg.to,"Me voy acercando y voy armando el plan") sendMessage(msg.to,"Sólo con pensarlo se acelera el pulso") sendMessage(msg.to,"Oh, yeah") sendMessage(msg.to,"Ya, ya me está gustando más de lo normal") sendMessage(msg.to,"Todos mis sentidos van pidiendo más") sendMessage(msg.to,"Esto hay que tomarlo sin ningún apuro") sendMessage(msg.to,"Des-pa-cito") sendMessage(msg.to,"Quiero respirar tu cuello despacito") sendMessage(msg.to,"Deja que te diga cosas al oído") sendMessage(msg.to,"Para que te acuerdes si no estás conmigo") sendMessage(msg.to,"Des-pa-cito") sendMessage(msg.to,"Quiero desnudarte a besos despacito") sendMessage(msg.to,"Firmo en las paredes de tu laberinto") sendMessage(msg.to,"Y hacer de tu cuerpo todo un manuscrito") sendMessage(msg.to,"Sube, sube, sube") sendMessage(msg.to,"Sube, sube") sendMessage(msg.to,"Quiero ver bailar tu pelo") sendMessage(msg.to,"Quiero ser tu ritmo") sendMessage(msg.to,"Que le enseñes a mi boca") sendMessage(msg.to,"Tus lugares favoritos") sendMessage(msg.to,"Déjame sobrepasar tus zonas de peligro") sendMessage(msg.to,"Hasta provocar tus gritos") sendMessage(msg.to,"Y que olvides tu apellido") sendMessage(msg.to,"Si te pido un beso ven dámelo") sendMessage(msg.to,"Yo sé que estás pensándolo") sendMessage(msg.to,"Llevo tiempo intentándolo") sendMessage(msg.to,"Mami, estoy dando y dándolo") sendMessage(msg.to,"Sabes que tu corazón conmigo te hace bom bom") sendMessage(msg.to,"Sabes que esa beba está buscando de mi bom bom") sendMessage(msg.to,"Ven prueba de mi boca para ver como te sabe") sendMessage(msg.to,"Quiero, quiero, quiero ver cuánto amor a ti te cabe") sendMessage(msg.to,"Yo no tengo prisa, yo me quiero dar el viaje") sendMessage(msg.to,"Empecemos lento, después salvaje") sendMessage(msg.to,"Pasito a pasito, suave suavecito") sendMessage(msg.to,"Nos vamos pegando, poquito a poquito") sendMessage(msg.to,"Cuando tú me besas con esa destreza") sendMessage(msg.to,"Veo que eres malicia con delicadeza") sendMessage(msg.to,"Pasito a pasito, suave suavecito") sendMessage(msg.to,"Nos vamos pegando, poquito a poquito") sendMessage(msg.to,"Y es que esa belleza es un rompecabezas") sendMessage(msg.to,"Pero pa' montarlo aquí tengo la pieza") sendMessage(msg.to,"Oye!") sendMessage(msg.to,"Des-pa-cito") sendMessage(msg.to,"Quiero respirar tu cuello despacito") sendMessage(msg.to,"Deja que te diga cosas al oído") sendMessage(msg.to,"Para que te acuerdes si no estás conmigo") sendMessage(msg.to,"Des-pa-cito") sendMessage(msg.to,"Quiero desnudarte a besos despacito") sendMessage(msg.to,"Firmo en las paredes de tu laberinto") sendMessage(msg.to,"Y hacer de tu cuerpo todo un manuscrito") sendMessage(msg.to,"Sube, sube, sube") sendMessage(msg.to,"Sube, sube") sendMessage(msg.to,"Quiero ver bailar tu pelo") sendMessage(msg.to,"Quiero ser tu ritmo") sendMessage(msg.to,"Que le enseñes a mi boca") sendMessage(msg.to,"Tus lugares favoritos") sendMessage(msg.to,"Déjame sobrepasar tus zonas de peligro") sendMessage(msg.to,"Hasta provocar tus gritos") sendMessage(msg.to,"Y que olvides tu apellido") sendMessage(msg.to,"Des-pa-cito") sendMessage(msg.to,"Vamos a hacerlo en una playa en Puerto Rico") sendMessage(msg.to,"Quiero respirar tu cuello despacito") sendMessage(msg.to,"Hasta que las olas griten "Ay, Bendito!"") sendMessage(msg.to,"Para que mi sello se quede contigo") sendMessage(msg.to,"Pasito a pasito, suave suavecito") sendMessage(msg.to,"Nos vamos pegando, poquito a poquito") sendMessage(msg.to,"Que le enseñes a mi boca") sendMessage(msg.to,"Tus lugares favoritos") sendMessage(msg.to,"Pasito a pasito, suave suavecito") sendMessage(msg.to,"Nos vamos pegando, poquito a poquito") sendMessage(msg.to,"Hasta provocar tus gritos") sendMessage(msg.to,"Y que olvides tu apellido") sendMessage(msg.to,"Des-pa-cito") sendMessage(msg.to,"Created By : PredatorsVoid") sendMessage(msg.to,"Thank You") #------------------------------------------------------------- if msg.text == "Tagall": group = client.getGroup(msg.to) mem = [contact.mid for contact in group.members] for mm in mem: xname = client.getContact(mm).displayName xlen = str(len(xname)+1) msg.contentType = 0 msg.text = "@"+xname+" " msg.contentMetadata ={'MENTION':'{"MENTIONEES":[{"S":"0","E":'+json.dumps(xlen)+',"M":'+json.dumps(mm)+'}]}','EMTVER':'4'} try: client.sendMessage(msg) except Exception as error: print error #------------------------------------------------------------- else: pass

except Exception as e:
    print e
    print ("\n\nSEND_MESSAGE\n\n")
    return
tracer.addOpInterrupt(25,SEND_MESSAGE)

while True: tracer.execute()
