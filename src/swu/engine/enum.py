#pylint: disable=multiple-statements

class Enum:
    def __hash__(self):
        return hash(self.__class__)

    def __eq__(self, other):
        return self.__class__ == other.__class__

    def __str__(self):
        return self.__class__.__name__

class AspectVigilance: pass # blue
class AspectCommand: pass # green
class AspectAggression: pass # red
class AspectCunning: pass # yellow
class AspectHeroism: pass
class AspectVillainy: pass


class ZoneDeck(Enum): pass
class ZoneDiscard(Enum): pass
class ZoneHand(Enum): pass
class ZoneSpace(Enum): pass
class ZoneGround(Enum): pass
class ZoneBase(Enum): pass
class ZoneLeader(Enum): pass
class ZoneResources(Enum): pass
class ZoneSideboard(Enum): pass


class PhaseSetup(Enum): pass
class PhaseAction(Enum): pass
class PhaseRegroup(Enum): pass


class ActionPlayCard(Enum): pass
class ActionAttack(Enum): pass
class ActionAbility(Enum): pass
class ActionTakeInitiative(Enum): pass
class ActionPass(Enum): pass
