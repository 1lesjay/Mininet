from mininet.topo import Topo

class MyTopo( Topo ):

	def __init__( self ):
	
		Topo.__init__( self )
		
		leftHost1 = self.addHost( 'h1' )
		leftHost2 = self.addHost( 'h2' )
		rightHost1 = self.addHost( 'h3' )
		rightHost2 = self.addHost( 'h4' )
		leftSwitch = self.addSwitch( 's1' )
		rightSwitch = self.addSwitch( 's2' ) 
		
		self.addLink( leftHost1, leftSwitch )
		self.addLink( leftHost2, leftSwitch )
		self.addLink( rightHost1, rightSwitch )
		self.addLink( rightHost2, rightSwitch )
		self.addLink( leftSwitch, rightSwitch )
		
		#self.addLink()
	
topos = { 'mytopo': ( lambda: MyTopo() ) }


