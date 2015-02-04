===========================================================================
Foreword
===========================================================================

.. raw:: latex

    \paragraph{\hfill{By Brett Cannon}}

When I joined the python-dev mailing list back in June 2002, the term "Python
3000" was brought out every few months to represent an idea the Python
development team wished they could act on, but for compatibility reasons could
not. Saying we could do something "maybe for Python 3000" meant it had no chance
of happening.

But then we started to say something could happen in Python 3000 more and more
often. Eventually it got to the point that "Python 3000" was referenced so often
on python-dev that the acronym "py3k" was created out of our inherent
programmer's laziness. Then we began to believe our own hype about what py3k
would be like and how much better it would be. It got to the point where Andrew
Kuchling created PEP 3100 (which was the original PEP 3000, which I eventually
took responsibility for) to keep track of the various ideas we had for py3k in
late 2004 as it was obvious around that time that we were actually going to go
through with the "crazy" idea of making Python 3000 happen. This all led to 
serious development starting in March 2006 and culminating in the release of
Python 3.0 on December 3, 2008.

While all of this was happening, there were mixed feelings from the community
about the feasibility/sanity of creating Python 3. When PEP 3100 was created in
2004, Python's popularity took a very noticeable uptick. This trend continued
and around 2006, when py3k development started in earnest, Python's popularity
exceeded that of Perl. So while Python was becoming one of the most popular
dynamic programming languages in the world, the development team was beginning
to create the next major version which would break compatibility with the
version of the language that all of these people were now learning. Some people
called us a little nuts for obvious reasons.

But we would like to think we knew what we were doing. While Python 2 is a great
language, Guido and everyone on the development team knew it had its flaws (if
it didn't then we would not have been able to create a PEP with nearly 100
things we wanted to change). Guido also realized that more Python code would be
written in the future then had been written to that point and into the future
that would continue to be true. As a service to our community (and partly
because it was fun) we decided we should try to fix some of our previous
mistakes so that future Python code could be written better and faster than was
possible with Python 2, hence why we created Python 3.

But while some considered us a little nuts to break compatibility with Python 2,
We also realized that we didn't want to leave our existing community behind and
develop Python 3 only for new code. The development team knew as we created
Python 3 that it was a superior language and so we wanted to share it with
everyone by making sure they could bring their Python 2 code with them into
their Python 3 work. From the beginning we made sure that the changes we made
could either be warned against in the worst case, and automated in the best.
Techniques we learned and tools we developed were used to port Python's
extensive standard library so as to learn from our own mistakes and make sure
that other people could port their own code. We always kept in the back of our
heads the goal of making porting Python 2 code as easy as possible.

The continual increase in the number of Python 3 projects available and the fact
that all of the major Linux distributions ship with Python 3, or will do so in
their next major release, is a testament that we didn't screw up. Guido always
said it would take 3 to 5 years for Python 3 to gain traction within the
community. The constant trend of Python 3 projects being released is a testament
that the timeline Guido set out is turning out to be true as major libraries
have already been ported, allowing their dependents to make the switch
themselves.

While some might question the utility in moving to Python 2 code to Python 3,
there are two things to keep in mind. One is that Python 3 is simply a nicer
language than Python 2. While there are only a handful of major changes, it's
all of the little changes that add up to make the experience of programming
Python 3 that much more pleasant compared to Python 2. It's rather common to
hear core developers say how they prefer coding in Python 3 over Python 2. I for
one have simply stopped coding in Python 2 as it just feels slightly off
compared to the more uniform feel of Python 3. And secondly, more code will be
written in Python 3 than in Python 2 over the history of the Python language, so
not porting means your project will eventually be left behind (this is already
starting to happen for projects which have publicly said they will not switch,
leading people to find alternatives for both their Python 2 and Python 3 code in
make sure they can switch to Python 3 when ready). Sitting idly by as the world
changes around you is not a good thing to do if you want to stay relevant.

I still remember the day that Python 3 was released. It was the end of the
workday and I was on IRC in #python-dev waiting for Barry Warsaw, the Python 3.0
release manager, to flip the switch on the release. When it was hit, I just
swivelled around in my chair and told Guido that it was done; Python 3 was no
longer a dream but an actual thing. I stood up, we gave each other an ecstatic
high-five, and just smiled (the next day people asked us at work what we were so
giddy about that night).

At that moment, and to this day, the thought that Python 3 would flop or not be
worth the amount of time and effort my fellow core developers and I put into it
never crossed my mind. And the fact that people care enough about seeing Python
3 work that there is now a book dedicated to helping people get from Python 2 to
Python 3 is a testament that Python 3 has not, and will not, flop.

.. raw:: latex

    \setcounter{secnumdepth}{2}
