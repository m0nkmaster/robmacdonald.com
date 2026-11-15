---
title: Global Collaboration in Software Engineering
description: How open source and big tech succeed with distributed teams through async communication, quality documentation, and customer focus.
date: 2025-03-14
original: https://www.linkedin.com/pulse/global-collaboration-software-engineering-rob-macdonald-ys1gf
---

Let me introduce the Synthstrom Deluge - a 'groove box'. It lets musicians create complete electronic music tracks from scratch. Electronic music has become my latest hobby and I love the Deluge, but what makes this device fascinating isn't my obsession with it. Two years ago, Synthstrom made a bold move: they released the device firmware as open source.

<figure><img src="/images/deluge.jpg" alt="The Synthstrom Deluge"><figcaption>Synthstrom Deluge - my new favourite toy</figcaption></figure>

The Deluge’s open source firmware development processes are _relaxed_ by corporate standards. No roadmaps, sprint planning, or formal hierarchies. Just a global group of musicians and programmers working across time zones. This isn't a simple project—it's sophisticated music hardware running complex C & C++ firmware handling audio processing to user interface design. Yet they're shipping features faster than many well-funded tech teams.

In the first year of being open source, there have been three high-quality releases introducing dozens of well-received new features.

This success story illustrates what I want to share about global software development.

---

Over 25 years, I've seen software development from several angles. From working in a four-person startup to heading up a team of 30+ at Amazon Prime Video. I've led teams across Poland, Slovakia, China, and the UK.

I've contributed to open source projects along the way, and what I've learnt is that the best practices in big-tech and open source are more similar than you think.

My thesis is simple: three fundamental principles drive the success of global collaborative working:

1. Asynchronous communication first
2. The importance of quality documentation
3. A clear customer focus.

These principles sound simple and obvious. But implementing them requires challenging deeply held assumptions about how good software teams work.

## Seeing Both Sides

I recently contributed to the Deluge project; adding new features, reviewing pull requests and realised I’m collaborating with developers from New Zealand to New York building complex software at scale, without many of the processes that we expect in our day jobs. No daily stand-ups. No quarterly planning. No ‘management’. But it’s working really well. My GitHub activity shows I’ve collaborated with over ten developers across various time zones in two months.

Thinking back, Amazon's structured corporate processes and open source's volunteer-led approach share similarities in their operations.

## Avoid Always-On Communication

> Hi! Got a minute? 👋

This is a bug bear of mine. We've replaced the in-person disruption of shoulder-tapping with the digital equivalent scaled x10 using Slack and Teams. The result? Engineers regularly context-switching, the stress of responding to "always-on" availability, and knowledge split across private messages and chat channels. This can work well with a close centrally located team, but it's a weakness at a global scale and during onboarding.

Open source takes a different approach. Most have a chat platform, but these are primarily used for chit-chat. Important communications happen in GitHub issues, discussions, and pull requests. Focused, single-threaded discussions that stay on topic and create a permanent record. No demand for an instant response.

While slower, this communication is more efficient, leading to faster progress. Without the ping-pong of chat messages and impromptu meetings, developers can maintain focus and manage their time. Important decisions get captured rather than buried in message threads. Teams across time zones can contribute equally, rather than being nudged into someone else's "standard" working hours. The playing field is levelled.

I recommend choosing minimal, integrated, async tools and sticking to them. Whether it’s GitHub, Jira, or something else, org-wide adoption and clear usage expectations matter. Amazon mostly uses internal tools - not the most feature-rich but adopted across the company from facilities, HR, to the teams owning the video streaming APIs, all teams use the same tools. And they are integrated into everything.

Knowledge accumulates naturally, becoming more refined and useful over time. Code repositories become not just a collection of code, but a living knowledge base that grows with the project.

This doesn't mean abandoning modern tools or returning to just emails. As leaders, it's about being intentional about team communication.

## Intentional Documentation

"Writing is thinking" - this mantra is drilled into every Amazonian. With teams across London and Beijing, I saw its importance. For every significant decision, product or technical, we'd write a two to six-page narrative document. The process was simple but powerful: write a proposal, circulate it for comments, and collect feedback. While we often reviewed these documents in meetings (with the famous 20-minute silent reading starts), being distributed, my teams had little in-office overlap. Alternatively, we ensured every stakeholder provided their comments before the author revised the document. We included a check box for each person to confirm they'd reviewed the document and communicated through annotated comments. This approach means:

- Engineers across time zones review proposals at their convenience.
- Non-native English speakers have time to process and respond thoughtfully.
- Knowledge accumulates into an evolving knowledge base.

It's fascinating how closely this mirrors successful open source projects. In the Deluge project, pull request checks enforce documentation updates. READMEs and Wikis are treated as code and product specifications, not afterthoughts. When I contributed a change recently, much of my PR’s discussion focused on improving documentation rather than implementation.

This documentation-first approach creates a self-sustaining cycle in corporate and open source environments. Knowledge becomes discoverable and persistent, unlike chat tool conversations.

PowerPoint isn't banned at Amazon, but I never wrote a presentation there. Presentations are synchronous and important information comes from discussions. Time is spent on making it look nice. A clear narrative forces precise thinking and a lasting record for revisiting.

## Customer Focus is key

Great documentation and async communication are powerful tools. But what motivates people to create and read docs? What drives engineers to write detailed pull requests, hold others accountable, and improve documentation?

In open source, the answer is clear. Contributors join projects like Deluge because they believe in what they're building, and they're often users of the software. Everyone understands why they are there.

When people care about the outcome, traditional management structures become less critical. We see this in successful open source projects; good practices emerge naturally because contributors care.

The open source community has been customer-focused from the start. It’s not just about finding the right tools or processes. The most important thing is that when everyone knows what they are building, why, and for who, collaboration comes for free and location becomes irrelevant.

This understanding is at Amazon’s core and summed up in their most often quoted [“Leadership Principle”](https://www.amazon.jobs/content/en/our-workplace/leadership-principles):  
  
Customer Obsession.

> “Leaders start with the customer and work backwards. They work vigorously to earn and keep customer trust. They obsess over customers.”

This is demonstrated in the PR FAQ (Press Release and Frequently Asked Questions) process, which is a key Amazon document that serves two main purposes: it validates that an idea solves a real customer need and captures the rationale for future reference.

## Summing up

Here are my thoughts: whether you’re managing a distributed corporate team or contributing to an open source project, the fundamentals remain the same: prioritise asynchronous communication, insist on quality documentation, and maintain a focus on the customer.

These principles work because they address the core challenges of global collaboration: time zone differences, knowledge sharing, and team alignment. When implemented thoughtfully, they create an environment where location is a non-issue.

## Next steps

Here are a few ideas to try out.

1. **Make Async Default**
  - Keep key information out of chat and in persistent docs.
  - Write complete questions instead of "Hi!" or "Got a minute?"
  - Make it clear that out-of-hours responses are not expected.
2. **Build a Documentation Culture**
  - Enforce document updates in pull requests and your definition of done.
  - Try a document read meeting instead of a presentation.
  - For remote teams, try async document reviews with checkboxes for stakeholders.
3. **Start with the Customer**
  - Try writing a PR-FAQ document for your next feature.
  - Run a “Walk the store” session - get your team using your product.

As leaders, we must model these approaches consistently and set clear expectations. Teams follow your example: if you respect people’s time, favour async communication, prioritise documentation, and demonstrate genuine customer focus, they will too.

Our behaviour shapes how global teams work together.
