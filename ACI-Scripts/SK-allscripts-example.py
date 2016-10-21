### THIS IS AN EXAMPLE OF SCRIPTS USED TO AUTOMATE DEPLOYMENT OF VLANS TO EPG/BD ON SK, ".txt" FILES ARE LISTS OF VLANS/ID/SUBNETS ###

### SCRIPT TO CREATE BD WITH SUBNET FOR L3 NETWORKS ###

with open('sak-vlanl3.txt') as f, open('sak-ipl3.txt') as g:
			for line,line2 in zip(f,g):
				line = line.rstrip('\n')
				line2 = line2.rstrip('\n')
				print ('\n<fvBD name="%s">\n<fvSubnet ip="%s" preferred="yes" scope="private" virtual="no"/>\n<fvRsCtx tnFvCtxName="SAK-DEFAULT"/>\n</fvBD>' %(line, line2))

### ASSIGN CONTRACT TO THE EPG - L3###

with open('sak-vlanl3.txt') as f:
	for line in f:
		line = line.rstrip('\n')
		print ('\n<fvAEPg name="%s">\n<fvRsBd tnFvBDName="%s"/>\n<fvRsCons tnVzBrCPName="ADM-PERMITALL"/>\n<fvRsProv tnVzBrCPName="ADM-PERMITALL"/>\n</fvAEPg>' %(line,line))

### CREATE EPG ON AP FOR L2 VLANS ###

with open('sak-vlanl2-dmz.txt') as f:
	for line in f:
		line = line.rstrip('\n')
		print ('\n<fvAEPg name="%s">\n<fvRsBd tnFvBDName="%s"/>\n</fvAEPg>' %(line,line))

### ASSIGN PHYDOM TO EPGS ###


print ('\n<fvTenant name="SAK-GMDC-1">')

print ('\n<fvAp name="SAK-ADM">')
with open('sak-vlanl3.txt') as f, open('sak-vlanl3-id.txt') as g:
	for line,line2 in zip(f,g):
		line = line.rstrip('\n')
		line2 = line2.rstrip('\n')
		print ('\n<fvAEPg name="%s">\n<fvRsDomAtt forceResolve="yes" instrImedcy="immediate" lcOwn="local" rn="rsdomAtt-[uni/phys-SAK-PHY]" tCl="physDomP" tDn="uni/phys-SAK-PHY"/>\n\n</fvAEPg>' %(line))
print ('\n</fvAp>')
print ('\n</fvTenant>')

### FULL SCRIPT FOR PATH ###


print ('\n<fvTenant name="SAK-GMDC-1">')

### L3 VLANS IN DEFAULT VRF ###

print ('\n<fvAp name="SAK-ADM">')
with open('sak-vlanl3.txt') as f, open('sak-vlanl3-id.txt') as g:
	for line,line2 in zip(f,g):
		line = line.rstrip('\n')
		line2 = line2.rstrip('\n')
		if line2 in ["45", "49", "52", "58", "63", "71", "110", "113", "115", "120", "125", "127", "129", "130", "145", "155", "160", "185", "221", "305", "310", "315", "320", "410"]:
			print ('\n<fvAEPg name="%s">\n<fvRsPathAtt encap="vlan-%s" instrImedcy="immediate" tDn="topology/pod-1/paths-101/pathep-[eth1/5]"/>\n</fvAEPg>' %(line,line2))
#		print ('\n<fvAEPg name="%s">\n<fvRsDomAtt instrImedcy="immediate" resImedcy="immediate" rn="rsdomAtt-[uni/phys-SAK-PHY]" tDn="uni/phys-SAK-PHY"/>\n</fvAEPg>' %(line))
#		print ('\n<fvAEPg name="%s">\n<fvRsPathAtt encap="vlan-%s" instrImedcy="immediate" rn="rspathAtt-[topology/pod-1/protpaths-103-104/pathep-[LEAF101-4-VPC-48_PolGrp]]" tDn="topology/pod-1/protpaths-103-104/pathep-[LEAF101-4-VPC-48_PolGrp]"/>\n</fvAEPg>' %(line,line2))
#		print ('\n<fvAEPg name="%s">\n<fvRsPathAtt encap="vlan-%s" instrImedcy="immediate" rn="rscEpToPathEp-[topology/pod-1/paths-104/pathep-[eth1/1]]" tDn="topology/pod-1/paths-104/pathep-[eth1/1]"/>\n</fvAEPg>' %(line,line2))
#		print ('\n<fvAEPg name="%s">\n<fvRsPathAtt encap="vlan-%s" instrImedcy="immediate" tDn="topology/pod-1/protpaths-101-102/pathep-[LEAF101-4-VPC-46]"/>\n</fvAEPg>' %(line,line2))
#		print ('\n<fvAEPg name="%s">\n<fvRsPathAtt encap="vlan-%s" instrImedcy="immediate" tDn="topology/pod-1/protpaths-101-102/pathep-[LEAF101-4-VPC-45]"/>\n</fvAEPg>' %(line,line2))
#		print ('\n<fvAEPg name="%s">\n<fvRsPathAtt encap="vlan-%s" instrImedcy="immediate" tDn="topology/pod-1/protpaths-103-104/pathep-[LEAF101-4-VPC-46]"/>\n</fvAEPg>' %(line,line2))
#		print ('\n<fvAEPg name="%s">\n<fvRsPathAtt encap="vlan-%s" instrImedcy="immediate" tDn="topology/pod-1/protpaths-103-104/pathep-[LEAF101-4-VPC-45]"/>\n</fvAEPg>' %(line,line2))
print ('\n</fvAp>')

### VLANS IN DMZ ###
print ('\n<fvAp name="SAK-DMZ">')
with open('sak-vlanl2-dmz.txt') as f, open('sak-vlanl2-dmz-id.txt') as g:
	for line,line2 in zip(f,g):
		line = line.rstrip('\n')
		line2 = line2.rstrip('\n')
		if line2 in ["45", "49", "52", "58", "63", "71", "110", "113", "115", "120", "125", "127", "129", "130", "145", "155", "160", "185", "221", "305", "310", "315", "320", "410"]:
			print ('\n<fvAEPg name="%s">\n<fvRsPathAtt encap="vlan-%s" instrImedcy="immediate" tDn="topology/pod-1/paths-101/pathep-[eth1/5]"/>\n</fvAEPg>' %(line,line2))
#		print ('\n<fvAEPg name="%s">\n<fvRsDomAtt instrImedcy="immediate" resImedcy="immediate" rn="rsdomAtt-[uni/phys-SAK-PHY]" tDn="uni/phys-SAK-PHY"/>\n</fvAEPg>' %(line))
#		print ('\n<fvAEPg name="%s">\n<fvRsBd tnFvBDName="%s"/>\n<fvRsPathAtt encap="vlan-%s" instrImedcy="immediate" rn="rspathAtt-[topology/pod-1/protpaths-103-104/pathep-[LEAF101-4-VPC-48_PolGrp]]" tDn="topology/pod-1/protpaths-103-104/pathep-[LEAF101-4-VPC-48_PolGrp]"/>\n</fvAEPg>' %(line,line,line2))
#		print ('\n<fvAEPg name="%s">\n<fvRsPathAtt encap="vlan-%s" instrImedcy="immediate" tDn="topology/pod-1/protpaths-101-102/pathep-[LEAF101-4-VPC-46]"/>\n</fvAEPg>' %(line,line2))
#		print ('\n<fvAEPg name="%s">\n<fvRsPathAtt encap="vlan-%s" instrImedcy="immediate" tDn="topology/pod-1/protpaths-101-102/pathep-[LEAF101-4-VPC-45]"/>\n</fvAEPg>' %(line,line2))
#		print ('\n<fvAEPg name="%s">\n<fvRsPathAtt encap="vlan-%s" instrImedcy="immediate" tDn="topology/pod-1/protpaths-103-104/pathep-[LEAF101-4-VPC-46]"/>\n</fvAEPg>' %(line,line2))
#		print ('\n<fvAEPg name="%s">\n<fvRsPathAtt encap="vlan-%s" instrImedcy="immediate" tDn="topology/pod-1/protpaths-103-104/pathep-[LEAF101-4-VPC-45]"/>\n</fvAEPg>' %(line,line2))
print ('\n</fvAp>')


### L2 VLANS - FIREWALL ###

print ('\n<fvAp name="FIREWALL">')
with open('sak-vlanl2-fw.txt') as f, open('sak-vlanl2-fw-id.txt') as g:
	for line,line2 in zip(f,g):
		line = line.rstrip('\n')
		line2 = line2.rstrip('\n')
		if line2 in ["45", "49", "52", "58", "63", "71", "110", "113", "115", "120", "125", "127", "129", "130", "145", "155", "160", "185", "221", "305", "310", "315", "320", "410"]:
			print ('\n<fvAEPg name="%s">\n<fvRsPathAtt encap="vlan-%s" instrImedcy="immediate" tDn="topology/pod-1/paths-101/pathep-[eth1/5]"/>\n</fvAEPg>' %(line,line2))
#		print ('\n<fvAEPg name="%s">\n<fvRsDomAtt instrImedcy="immediate" resImedcy="immediate" rn="rsdomAtt-[uni/phys-SAK-PHY]" tDn="uni/phys-SAK-PHY"/>\n</fvAEPg>' %(line))
#		print ('\n<fvAEPg name="%s">\n<fvRsPathAtt encap="vlan-%s" instrImedcy="immediate" rn="rspathAtt-[topology/pod-1/protpaths-103-104/pathep-[LEAF101-4-VPC-48_PolGrp]]" tDn="topology/pod-1/protpaths-103-104/pathep-[LEAF101-4-VPC-48_PolGrp]"/>\n</fvAEPg>' %(line,line2))
#		print ('\n<fvAEPg name="%s">\n<fvRsPathAtt encap="vlan-%s" instrImedcy="immediate" tDn="topology/pod-1/protpaths-101-102/pathep-[LEAF101-4-VPC-46]"/>\n</fvAEPg>' %(line,line2))
#		print ('\n<fvAEPg name="%s">\n<fvRsPathAtt encap="vlan-%s" instrImedcy="immediate" tDn="topology/pod-1/protpaths-101-102/pathep-[LEAF101-4-VPC-45]"/>\n</fvAEPg>' %(line,line2))
#		print ('\n<fvAEPg name="%s">\n<fvRsPathAtt encap="vlan-%s" instrImedcy="immediate" tDn="topology/pod-1/protpaths-103-104/pathep-[LEAF101-4-VPC-46]"/>\n</fvAEPg>' %(line,line2))
#		print ('\n<fvAEPg name="%s">\n<fvRsPathAtt encap="vlan-%s" instrImedcy="immediate" tDn="topology/pod-1/protpaths-103-104/pathep-[LEAF101-4-VPC-45]"/>\n</fvAEPg>' %(line,line2))
print ('\n</fvAp>')

### L2 VLANS - GUEST ###

print ('\n<fvAp name="GUEST">')
with open('sak-vlanl2-guest.txt') as f, open('sak-vlanl2-guest-id.txt') as g:
	for line,line2 in zip(f,g):
		line = line.rstrip('\n')
		line2 = line2.rstrip('\n')
		if line2 in ["45", "49", "52", "58", "63", "71", "110", "113", "115", "120", "125", "127", "129", "130", "145", "155", "160", "185", "221", "305", "310", "315", "320", "410"]:
			print ('\n<fvAEPg name="%s">\n<fvRsPathAtt encap="vlan-%s" instrImedcy="immediate" tDn="topology/pod-1/paths-101/pathep-[eth1/5]"/>\n</fvAEPg>' %(line,line2))
#		print ('\n<fvAEPg name="%s">\n<fvRsDomAtt instrImedcy="immediate" resImedcy="immediate" rn="rsdomAtt-[uni/phys-SAK-PHY]" tDn="uni/phys-SAK-PHY"/>\n</fvAEPg>' %(line))
#		print ('\n<fvAEPg name="%s">\n<fvRsPathAtt encap="vlan-%s" instrImedcy="immediate" rn="rspathAtt-[topology/pod-1/protpaths-103-104/pathep-[LEAF101-4-VPC-48_PolGrp]]" tDn="topology/pod-1/protpaths-103-104/pathep-[LEAF101-4-VPC-48_PolGrp]"/>\n</fvAEPg>' %(line,line2))
#		print ('\n<fvAEPg name="%s">\n<fvRsPathAtt encap="vlan-%s" instrImedcy="immediate" tDn="topology/pod-1/protpaths-101-102/pathep-[LEAF101-4-VPC-46]"/>\n</fvAEPg>' %(line,line2))
#		print ('\n<fvAEPg name="%s">\n<fvRsPathAtt encap="vlan-%s" instrImedcy="immediate" tDn="topology/pod-1/protpaths-101-102/pathep-[LEAF101-4-VPC-45]"/>\n</fvAEPg>' %(line,line2))
#		print ('\n<fvAEPg name="%s">\n<fvRsPathAtt encap="vlan-%s" instrImedcy="immediate" tDn="topology/pod-1/protpaths-103-104/pathep-[LEAF101-4-VPC-46]"/>\n</fvAEPg>' %(line,line2))
#		print ('\n<fvAEPg name="%s">\n<fvRsPathAtt encap="vlan-%s" instrImedcy="immediate" tDn="topology/pod-1/protpaths-103-104/pathep-[LEAF101-4-VPC-45]"/>\n</fvAEPg>' %(line,line2))
print ('\n</fvAp>')

### L2 VLANS - HELSE L2 ###

print ('\n<fvAp name="HELSE-L2">')
with open('sak-vlanl2-helse.txt') as f, open('sak-vlanl2-helse-id.txt') as g:
	for line,line2 in zip(f,g):
		line = line.rstrip('\n')
		line2 = line2.rstrip('\n')
		if line2 in ["45", "49", "52", "58", "63", "71", "110", "113", "115", "120", "125", "127", "129", "130", "145", "155", "160", "185", "221", "305", "310", "315", "320", "410"]:
			print ('\n<fvAEPg name="%s">\n<fvRsPathAtt encap="vlan-%s" instrImedcy="immediate" tDn="topology/pod-1/paths-101/pathep-[eth1/5]"/>\n</fvAEPg>' %(line,line2))
#		print ('\n<fvAEPg name="%s">\n<fvRsDomAtt instrImedcy="immediate" resImedcy="immediate" rn="rsdomAtt-[uni/phys-SAK-PHY]" tDn="uni/phys-SAK-PHY"/>\n</fvAEPg>' %(line))
#		print ('\n<fvAEPg name="%s">\n<fvRsPathAtt encap="vlan-%s" instrImedcy="immediate" rn="rspathAtt-[topology/pod-1/protpaths-103-104/pathep-[LEAF101-4-VPC-48_PolGrp]]" tDn="topology/pod-1/protpaths-103-104/pathep-[LEAF101-4-VPC-48_PolGrp]"/>\n</fvAEPg>' %(line,line2))
#		print ('\n<fvAEPg name="%s">\n<fvRsPathAtt encap="vlan-%s" instrImedcy="immediate" tDn="topology/pod-1/protpaths-101-102/pathep-[LEAF101-4-VPC-46]"/>\n</fvAEPg>' %(line,line2))
#		print ('\n<fvAEPg name="%s">\n<fvRsPathAtt encap="vlan-%s" instrImedcy="immediate" tDn="topology/pod-1/protpaths-101-102/pathep-[LEAF101-4-VPC-45]"/>\n</fvAEPg>' %(line,line2))
	#	print ('\n<fvAEPg name="%s">\n<fvRsPathAtt encap="vlan-%s" instrImedcy="immediate" tDn="topology/pod-1/protpaths-103-104/pathep-[LEAF101-4-VPC-46]"/>\n</fvAEPg>' %(line,line2))
#		print ('\n<fvAEPg name="%s">\n<fvRsPathAtt encap="vlan-%s" instrImedcy="immediate" tDn="topology/pod-1/protpaths-103-104/pathep-[LEAF101-4-VPC-45]"/>\n</fvAEPg>' %(line,line2))
print ('\n</fvAp>')

## L2 VLANS - LINKNETS ###

print ('\n<fvAp name="LINKNETT">')
with open('sak-vlanl2-linknet.txt') as f, open('sak-vlanl2-linknet-id.txt') as g:
	for line,line2 in zip(f,g):
		line = line.rstrip('\n')
		line2 = line2.rstrip('\n')
		if line2 in ["45", "49", "52", "58", "63", "71", "110", "113", "115", "120", "125", "127", "129", "130", "145", "155", "160", "185", "221", "305", "310", "315", "320", "410"]:
			print ('\n<fvAEPg name="%s">\n<fvRsPathAtt encap="vlan-%s" instrImedcy="immediate" tDn="topology/pod-1/paths-101/pathep-[eth1/5]"/>\n</fvAEPg>' %(line,line2))
#		print ('\n<fvAEPg name="%s">\n<fvRsDomAtt instrImedcy="immediate" resImedcy="immediate" rn="rsdomAtt-[uni/phys-SAK-PHY]" tDn="uni/phys-SAK-PHY"/>\n</fvAEPg>' %(line))
#		print ('\n<fvAEPg name="%s">\n<fvRsPathAtt encap="vlan-%s" instrImedcy="immediate" rn="rspathAtt-[topology/pod-1/protpaths-103-104/pathep-[LEAF101-4-VPC-48_PolGrp]]" tDn="topology/pod-1/protpaths-103-104/pathep-[LEAF101-4-VPC-48_PolGrp]"/>\n</fvAEPg>' %(line,line2))
#		print ('\n<fvAEPg name="%s">\n<fvRsPathAtt encap="vlan-%s" instrImedcy="immediate" tDn="topology/pod-1/protpaths-101-102/pathep-[LEAF101-4-VPC-46]"/>\n</fvAEPg>' %(line,line2))
#		print ('\n<fvAEPg name="%s">\n<fvRsPathAtt encap="vlan-%s" instrImedcy="immediate" tDn="topology/pod-1/protpaths-101-102/pathep-[LEAF101-4-VPC-45]"/>\n</fvAEPg>' %(line,line2))
#		print ('\n<fvAEPg name="%s">\n<fvRsPathAtt encap="vlan-%s" instrImedcy="immediate" tDn="topology/pod-1/protpaths-103-104/pathep-[LEAF101-4-VPC-46]"/>\n</fvAEPg>' %(line,line2))
#		print ('\n<fvAEPg name="%s">\n<fvRsPathAtt encap="vlan-%s" instrImedcy="immediate" tDn="topology/pod-1/protpaths-103-104/pathep-[LEAF101-4-VPC-45]"/>\n</fvAEPg>' %(line,line2))
print ('\n</fvAp>')

## L2 VLANS - TEST NETT##

print ('\n<fvAp name="TESTNETT">')
with open('sak-vlanl2-test.txt') as f, open('sak-vlanl2-test-id.txt') as g:
	for line,line2 in zip(f,g):
		line = line.rstrip('\n')
		line2 = line2.rstrip('\n')
		if line2 in ["45", "49", "52", "58", "63", "71", "110", "113", "115", "120", "125", "127", "129", "130", "145", "155", "160", "185", "221", "305", "310", "315", "320", "410"]:
			print ('\n<fvAEPg name="%s">\n<fvRsPathAtt encap="vlan-%s" instrImedcy="immediate" tDn="topology/pod-1/paths-101/pathep-[eth1/5]"/>\n</fvAEPg>' %(line,line2))
#		print ('\n<fvAEPg name="%s">\n<fvRsDomAtt instrImedcy="immediate" resImedcy="immediate" rn="rsdomAtt-[uni/phys-SAK-PHY]" tDn="uni/phys-SAK-PHY"/>\n</fvAEPg>' %(line))
#		print ('\n<fvAEPg name="%s">\n<fvRsPathAtt encap="vlan-%s" instrImedcy="immediate" rn="rspathAtt-[topology/pod-1/protpaths-103-104/pathep-[LEAF101-4-VPC-48_PolGrp]]" tDn="topology/pod-1/protpaths-103-104/pathep-[LEAF101-4-VPC-48_PolGrp]"/>\n</fvAEPg>' %(line,line2))
#		print ('\n<fvAEPg name="%s">\n<fvRsPathAtt encap="vlan-%s" instrImedcy="immediate" tDn="topology/pod-1/protpaths-101-102/pathep-[LEAF101-4-VPC-46]"/>\n</fvAEPg>' %(line,line2))
#		print ('\n<fvAEPg name="%s">\n<fvRsPathAtt encap="vlan-%s" instrImedcy="immediate" tDn="topology/pod-1/protpaths-101-102/pathep-[LEAF101-4-VPC-45]"/>\n</fvAEPg>' %(line,line2))
#		print ('\n<fvAEPg name="%s">\n<fvRsPathAtt encap="vlan-%s" instrImedcy="immediate" tDn="topology/pod-1/protpaths-103-104/pathep-[LEAF101-4-VPC-46]"/>\n</fvAEPg>' %(line,line2))
#		print ('\n<fvAEPg name="%s">\n<fvRsPathAtt encap="vlan-%s" instrImedcy="immediate" tDn="topology/pod-1/protpaths-103-104/pathep-[LEAF101-4-VPC-45]"/>\n</fvAEPg>' %(line,line2))
print ('\n</fvAp>')

## L2 VLANS - OTHERS ##

print ('\n<fvAp name="OTHER-L2">')
with open('sak-vlanl2-other.txt') as f, open('sak-vlanl2-other-id.txt') as g:
	for line,line2 in zip(f,g):
		line = line.rstrip('\n')
		line2 = line2.rstrip('\n')
		if line2 in ["45", "49", "52", "58", "63", "71", "110", "113", "115", "120", "125", "127", "129", "130", "145", "155", "160", "185", "221", "305", "310", "315", "320", "410"]:
			print ('\n<fvAEPg name="%s">\n<fvRsPathAtt encap="vlan-%s" instrImedcy="immediate" tDn="topology/pod-1/paths-101/pathep-[eth1/5]"/>\n</fvAEPg>' %(line,line2))
#		print ('\n<fvAEPg name="%s">\n<fvRsDomAtt instrImedcy="immediate" resImedcy="immediate" rn="rsdomAtt-[uni/phys-SAK-PHY]" tDn="uni/phys-SAK-PHY"/>\n</fvAEPg>' %(line))
#		print ('\n<fvAEPg name="%s">\n<fvRsPathAtt encap="vlan-%s" instrImedcy="immediate" rn="rspathAtt-[topology/pod-1/protpaths-103-104/pathep-[LEAF101-4-VPC-48_PolGrp]]" tDn="topology/pod-1/protpaths-103-104/pathep-[LEAF101-4-VPC-48_PolGrp]"/>\n</fvAEPg>' %(line,line2))
#		print ('\n<fvAEPg name="%s">\n<fvRsPathAtt encap="vlan-%s" instrImedcy="immediate" tDn="topology/pod-1/protpaths-101-102/pathep-[LEAF101-4-VPC-46]"/>\n</fvAEPg>' %(line,line2))
#		print ('\n<fvAEPg name="%s">\n<fvRsPathAtt encap="vlan-%s" instrImedcy="immediate" tDn="topology/pod-1/protpaths-101-102/pathep-[LEAF101-4-VPC-45]"/>\n</fvAEPg>' %(line,line2))
#		print ('\n<fvAEPg name="%s">\n<fvRsPathAtt encap="vlan-%s" instrImedcy="immediate" tDn="topology/pod-1/protpaths-103-104/pathep-[LEAF101-4-VPC-46]"/>\n</fvAEPg>' %(line,line2))
#		print ('\n<fvAEPg name="%s">\n<fvRsPathAtt encap="vlan-%s" instrImedcy="immediate" tDn="topology/pod-1/protpaths-103-104/pathep-[LEAF101-4-VPC-45]"/>\n</fvAEPg>' %(line,line2))
print ('\n</fvAp>')

### VLANS IN OTHER VRFS ###

## VRF HELSENETT ###

print ('\n<fvAp name="HELSENETT">')
with open('sak-vlanl3-helse.txt') as f, open('sak-vlanl3-helse-id.txt') as g:
	for line,line2 in zip(f,g):
		line = line.rstrip('\n')
		line2 = line2.rstrip('\n')
		if line2 in ["45", "49", "52", "58", "63", "71", "110", "113", "115", "120", "125", "127", "129", "130", "145", "155", "160", "185", "221", "305", "310", "315", "320", "410"]:
			print ('\n<fvAEPg name="%s">\n<fvRsPathAtt encap="vlan-%s" instrImedcy="immediate" tDn="topology/pod-1/paths-101/pathep-[eth1/5]"/>\n</fvAEPg>' %(line,line2))
#		print ('\n<fvAEPg name="%s">\n<fvRsDomAtt instrImedcy="immediate" resImedcy="immediate" rn="rsdomAtt-[uni/phys-SAK-PHY]" tDn="uni/phys-SAK-PHY"/>\n</fvAEPg>' %(line))
#		print ('\n<fvAEPg name="%s">\n<fvRsPathAtt encap="vlan-%s" instrImedcy="immediate" rn="rspathAtt-[topology/pod-1/protpaths-103-104/pathep-[LEAF101-4-VPC-48_PolGrp]]" tDn="topology/pod-1/protpaths-103-104/pathep-[LEAF101-4-VPC-48_PolGrp]"/>\n</fvAEPg>' %(line,line2))
#		print ('\n<fvAEPg name="%s">\n<fvRsPathAtt encap="vlan-%s" instrImedcy="immediate" tDn="topology/pod-1/protpaths-101-102/pathep-[LEAF101-4-VPC-46]"/>\n</fvAEPg>' %(line,line2))
#		print ('\n<fvAEPg name="%s">\n<fvRsPathAtt encap="vlan-%s" instrImedcy="immediate" tDn="topology/pod-1/protpaths-101-102/pathep-[LEAF101-4-VPC-45]"/>\n</fvAEPg>' %(line,line2))
#		print ('\n<fvAEPg name="%s">\n<fvRsPathAtt encap="vlan-%s" instrImedcy="immediate" tDn="topology/pod-1/protpaths-103-104/pathep-[LEAF101-4-VPC-46]"/>\n</fvAEPg>' %(line,line2))
#		print ('\n<fvAEPg name="%s">\n<fvRsPathAtt encap="vlan-%s" instrImedcy="immediate" tDn="topology/pod-1/protpaths-103-104/pathep-[LEAF101-4-VPC-45]"/>\n</fvAEPg>' %(line,line2))
print ('\n</fvAp>')

### VRF NAV ###
print ('\n<fvAp name="NAV">')
with open('sak-vlanl3-nav.txt') as f, open('sak-vlanl3-nav-id.txt') as g:
	for line,line2 in zip(f,g):
		line = line.rstrip('\n')
		line2 = line2.rstrip('\n')
		if line2 in ["45", "49", "52", "58", "63", "71", "110", "113", "115", "120", "125", "127", "129", "130", "145", "155", "160", "185", "221", "305", "310", "315", "320", "410"]:
			print ('\n<fvAEPg name="%s">\n<fvRsPathAtt encap="vlan-%s" instrImedcy="immediate" tDn="topology/pod-1/paths-101/pathep-[eth1/5]"/>\n</fvAEPg>' %(line,line2))
#		print ('\n<fvAEPg name="%s">\n<fvRsDomAtt instrImedcy="immediate" resImedcy="immediate" rn="rsdomAtt-[uni/phys-SAK-PHY]" tDn="uni/phys-SAK-PHY"/>\n</fvAEPg>' %(line))
#		print ('\n<fvAEPg name="%s">\n<fvRsPathAtt encap="vlan-%s" instrImedcy="immediate" rn="rspathAtt-[topology/pod-1/protpaths-103-104/pathep-[LEAF101-4-VPC-48_PolGrp]]" tDn="topology/pod-1/protpaths-103-104/pathep-[LEAF101-4-VPC-48_PolGrp]"/>\n</fvAEPg>' %(line,line2))
#		print ('\n<fvAEPg name="%s">\n<fvRsPathAtt encap="vlan-%s" instrImedcy="immediate" tDn="topology/pod-1/protpaths-101-102/pathep-[LEAF101-4-VPC-46]"/>\n</fvAEPg>' %(line,line2))
#		print ('\n<fvAEPg name="%s">\n<fvRsPathAtt encap="vlan-%s" instrImedcy="immediate" tDn="topology/pod-1/protpaths-101-102/pathep-[LEAF101-4-VPC-45]"/>\n</fvAEPg>' %(line,line2))
#		print ('\n<fvAEPg name="%s">\n<fvRsPathAtt encap="vlan-%s" instrImedcy="immediate" tDn="topology/pod-1/protpaths-103-104/pathep-[LEAF101-4-VPC-46]"/>\n</fvAEPg>' %(line,line2))
#		print ('\n<fvAEPg name="%s">\n<fvRsPathAtt encap="vlan-%s" instrImedcy="immediate" tDn="topology/pod-1/protpaths-103-104/pathep-[LEAF101-4-VPC-45]"/>\n</fvAEPg>' %(line,line2))
print ('\n</fvAp>')

### VRF NORDICCONNECT ###

print ('\n<fvAp name="NORDICCONNECT">')
with open('sak-vlanl3-nordic.txt') as f, open('sak-vlanl3-nordic-id.txt') as g:
	for line,line2 in zip(f,g):
		line = line.rstrip('\n')
		line2 = line2.rstrip('\n')
		if line2 in ["45", "49", "52", "58", "63", "71", "110", "113", "115", "120", "125", "127", "129", "130", "145", "155", "160", "185", "221", "305", "310", "315", "320", "410"]:
			print ('\n<fvAEPg name="%s">\n<fvRsPathAtt encap="vlan-%s" instrImedcy="immediate" tDn="topology/pod-1/paths-101/pathep-[eth1/5]"/>\n</fvAEPg>' %(line,line2))
#		print ('\n<fvAEPg name="%s">\n<fvRsDomAtt instrImedcy="immediate" resImedcy="immediate" rn="rsdomAtt-[uni/phys-SAK-PHY]" tDn="uni/phys-SAK-PHY"/>\n</fvAEPg>' %(line))
#		print ('\n<fvAEPg name="%s">\n<fvRsPathAtt encap="vlan-%s" instrImedcy="immediate" rn="rspathAtt-[topology/pod-1/protpaths-103-104/pathep-[LEAF101-4-VPC-48_PolGrp]]" tDn="topology/pod-1/protpaths-103-104/pathep-[LEAF101-4-VPC-48_PolGrp]"/>\n</fvAEPg>' %(line,line2))
#		print ('\n<fvAEPg name="%s">\n<fvRsPathAtt encap="vlan-%s" instrImedcy="immediate" tDn="topology/pod-1/protpaths-101-102/pathep-[LEAF101-4-VPC-46]"/>\n</fvAEPg>' %(line,line2))
#		print ('\n<fvAEPg name="%s">\n<fvRsPathAtt encap="vlan-%s" instrImedcy="immediate" tDn="topology/pod-1/protpaths-101-102/pathep-[LEAF101-4-VPC-45]"/>\n</fvAEPg>' %(line,line2))
#		print ('\n<fvAEPg name="%s">\n<fvRsPathAtt encap="vlan-%s" instrImedcy="immediate" tDn="topology/pod-1/protpaths-103-104/pathep-[LEAF101-4-VPC-46]"/>\n</fvAEPg>' %(line,line2))
#		print ('\n<fvAEPg name="%s">\n<fvRsPathAtt encap="vlan-%s" instrImedcy="immediate" tDn="topology/pod-1/protpaths-103-104/pathep-[LEAF101-4-VPC-45]"/>\n</fvAEPg>' %(line,line2))
print ('\n</fvAp>')

#####

print ('\n</fvTenant>')