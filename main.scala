import chisel3._
import circt.stage.ChiselStage
import java.io._

class Echo(width: Int) extends Module {
  val io = IO(new Bundle {
    val fake_adc  = Input(UInt(width.W))
    val fake_dac = Output(UInt(width.W))
  })

  val delay = RegInit(UInt(width.W), 0.U)
  delay := io.fake_adc
  io.fake_dac := delay
}

object Hello {
  def main(args: Array[String]) : Unit = {
    val writer = new FileWriter(new File("echo.sv"))
    val sv = ChiselStage.emitSystemVerilog(new Echo(args(0).toInt))
    writer.write(sv)
    writer.close()
  }
}
