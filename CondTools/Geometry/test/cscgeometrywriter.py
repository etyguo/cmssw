import FWCore.ParameterSet.Config as cms

process = cms.Process("CSCGeometryWriter")
process.load('CondCore.DBCommon.CondDBCommon_cfi')
process.load('Configuration.StandardSequences.GeometryExtended_cff')
process.load('Geometry.MuonNumbering.muonNumberingInitialization_cfi')

process.source = cms.Source("EmptyIOVSource",
                            lastValue = cms.uint64(1),
                            timetype = cms.string('runnumber'),
                            firstValue = cms.uint64(1),
                            interval = cms.uint64(1)
                            )

process.CSCGeometryWriter = cms.EDAnalyzer("CSCRecoIdealDBLoader")

process.CondDBCommon.BlobStreamerName = cms.untracked.string('TBufferBlobStreamingService')
process.CondDBCommon.timetype = cms.untracked.string('runnumber')
process.CondDBCommon.connect = cms.string('sqlite_file:myfile.db')
process.PoolDBOutputService = cms.Service("PoolDBOutputService",
                                          process.CondDBCommon,
                                          toPut = cms.VPSet(cms.PSet(record = cms.string('CSCRecoGeometryRcd'),tag = cms.string('CSCRECO_Geometry_Test01')),
                                                            cms.PSet(record = cms.string('CSCRecoDigiParametersRcd'),tag = cms.string('CSCRECODIGI_Geometry_Test01')))
                                          )

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(1)
    )

process.p1 = cms.Path(process.CSCGeometryWriter)
