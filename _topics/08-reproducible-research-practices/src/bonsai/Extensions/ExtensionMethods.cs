using System;

namespace Experimentgonogo
{
    public partial class Trial
    {
        public virtual TimeSpan ToInterTrialInterval()
        {
            throw new NotImplementedException();
        }
    }

    public partial class NoGoTrial
    {
        public override TimeSpan ToInterTrialInterval()
        {
            return TimeSpan.FromSeconds(this.InterTrialInterval);
        }
    }

    public partial class GoTrial
    {
        public override TimeSpan ToInterTrialInterval()
        {
            if (this.Cue == "Foo")
            {
                return TimeSpan.FromSeconds(this.InterTrialInterval + 1);
            }
            else
            {
                return TimeSpan.FromSeconds(this.InterTrialInterval);
            }
        }
    }

}