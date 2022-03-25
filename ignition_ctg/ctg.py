# adds a PointID (data point) to graph
def addGraphPoint(pid):
	import fpmi, app
	app.ctg.deleteGraphPoint(pid)
	cid = fpmi.system.getClientId()	
	fpmi.db.runPrepStmt("INSERT INTO ctg_active_client (PointID, Client_ID) VALUES (?,?)" , [pid,cid])
	app.ctg.updateGraph(-1)

# deletes a PointID (data point) from a graph
def deleteGraphPoint(pid):
	import fpmi, app
	cid = fpmi.system.getClientId()
	fpmi.db.runPrepStmt("DELETE FROM ctg_active_client WHERE PointID = ? AND Client_ID = ?" , [pid,cid])
	app.ctg.updateGraph(-1)

# Clears all PointID's (data points) from graph
def clearGraphPoints():	
	import fpmi, app
	cid = fpmi.system.getClientId()	
	fpmi.db.runPrepStmt("DELETE FROM ctg_active_client WHERE Client_ID = ?", [cid])
	app.ctg.updateGraph(-1)

# generates pop up menu when an object is right clicked
def showPopup(event):
	import fpmi

	pid = event.source.getPropertyValue("PointID") # defined at object
	pidName = fpmi.db.runScalarQuery("SELECT NAME FROM ctg_pens WHERE PointID = '%s'" % pid)
	if pidName == None:
		pidName = pid

	menuNames = []
	menuFunctions = []

	def fake(event):
		pass

	menuNames.append("<html><i>%s" % pidName)
	menuFunctions.append(fake)
	menuNames.append("sep")
	menuFunctions.append(None)

	#check if the point is already there
	cid = fpmi.system.getClientId()	
	pid = event.source.getPropertyValue("PointID")
	probe=fpmi.db.runQuery("SELECT 1 FROM ctg_active_client WHERE PointID = '%s' and Client_ID = '%s'" % (pid, cid))
	if len(probe)==0:
		def addToCGraph(event):
			import app
			pid = event.source.getPropertyValue("PointID")
			app.ctg.addGraphPoint(pid)
		menuNames.append("<html>(+) Add to Graph")
		menuFunctions.append(addToCGraph)

	else:
		def subFromCGraph(event):
			import app
			pid = event.source.getPropertyValue("PointID")
			app.ctg.deleteGraphPoint(pid)
		menuNames.append("<html>(-)  Remove from Graph")
		menuFunctions.append(subFromCGraph)

	menuNames.append("sep")
	menuFunctions.append(None)

	def clearGraph(event):
		import app
		app.ctg.clearGraphPoints()

	menuNames.append("Clear Current Graph")
	menuFunctions.append(clearGraph)

	def openGraph(event):
		import app
		app.ctg.openCurrentGraph()

	menuNames.append("Open Current Graph")
	menuFunctions.append(openGraph)

	popupMenu = fpmi.gui.createPopupMenu(menuNames, menuFunctions)
	popupMenu.show(event)

# Opens the graph window
def openCurrentGraph():
	import fpmi
	fpmi.nav.openWindow("CTG_Graph")
	fpmi.nav.centerWindow("CTG_Graph")

# Updates the easy chart in the graph window
def updateGraph(graphID = None):
	import fpmi
	try:
		window = fpmi.gui.getWindow("CTG_Graph")
		if window != None:
			graph = window.rootContainer.getComponent("ctg_Chart")
			dropdown = window.rootContainer.getComponent("Box").getComponent("SavedGraphs")
			fpmi.db.refresh(graph, "tagPens")
			fpmi.db.refresh(graph, "pens")
			fpmi.db.refresh(graph, "axes")
			fpmi.db.refresh(graph, "subplots")
			fpmi.db.refresh(dropdown, "data")

			if graphID != None:
				window.rootContainer.LoadedGraphID = graphID
	except:
		pass
	
# Gets a list of VALID datasources and databases
def getDataSources():
	import system
	connections = system.dataset.toPyDataSet(system.db.getConnections())	
	databases = []
	datasources = []
	index = 0
	for con in connections:
		if con["Status"].upper() == "VALID" or con["Status"] == "":
			datasources.append([index, con["Name"]])
			try:
				if con["DBType"] == "MYSQL":
					databases.append([index, system.db.runScalarQuery("SELECT DATABASE()", con["Name"]) + "."])
				elif con["DBType"] == "MSSQL":
					databases.append([index, system.db.runScalarQuery("SELECT DB_NAME()", con["Name"]) + ".dbo."])	
			except:
				print "Error getting DBName"
			index += 1
	return (datasources, databases)

# Updates properties with database info
def initializeDataSources(window):
	import system, fpmi, app
	win = system.gui.getWindow(window)
	data = app.ctg.getDataSources()
	win.rootContainer.datasources = fpmi.db.toDataSet(["Index", "DataSource"], data[0])
	win.rootContainer.databases = fpmi.db.toDataSet(["Index", "Database"], data[1])
	return 1


