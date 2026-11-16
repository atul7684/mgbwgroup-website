import type { Metadata } from "next";

export const metadata: Metadata = {
  title: "Privacy Policy | MGBW Group",
  description: "Privacy Policy for MGBW Group website.",
};

export default function PrivacyPage() {
  return (
    <section className="py-20 px-4 bg-white">
      <div className="max-w-3xl mx-auto prose prose-gray">
        <h1>Privacy Policy</h1>
        <p>
          At <strong>MGBW Group</strong>, we respect your privacy and are
          committed to protecting the personal information you share with us.
          This Privacy Policy explains how we collect, use, and safeguard your
          data when you visit our website or interact with our services.
        </p>

        <h2>1. Information We Collect</h2>
        <p>We may collect the following information when you use our website:</p>
        <ul>
          <li>Personal details (name, email, phone) when you submit inquiries or contact forms.</li>
          <li>Business information if you apply to join our distributor or partner network.</li>
          <li>Technical information (IP address, browser type, browsing data) through cookies or analytics.</li>
        </ul>

        <h2>2. How We Use Your Information</h2>
        <ul>
          <li>Respond to your inquiries and requests.</li>
          <li>Process distributor or partnership applications.</li>
          <li>Share updates about our services, businesses, or events (if you opt in).</li>
          <li>Improve the performance and functionality of our website.</li>
          <li>Comply with applicable legal obligations.</li>
        </ul>

        <h2>3. How We Protect Your Information</h2>
        <p>
          We implement industry-standard security measures to safeguard your
          personal data from unauthorized access, disclosure, or misuse.
        </p>

        <h2>4. Sharing of Information</h2>
        <p>
          We do not sell, rent, or trade your personal information to third
          parties. We may share limited data only with service providers who
          assist us in operating our website, or regulatory authorities if
          required by law.
        </p>

        <h2>5. Cookies &amp; Analytics</h2>
        <p>
          Our website may use cookies and analytics tools to enhance your
          browsing experience. You can control or disable cookies through your
          browser settings.
        </p>

        <h2>6. Third-Party Links</h2>
        <p>
          Our website may contain links to external websites. We are not
          responsible for the privacy practices of these third parties.
        </p>

        <h2>7. Your Rights</h2>
        <ul>
          <li>Request access to the personal information we hold about you.</li>
          <li>Ask for corrections or deletion of your data.</li>
          <li>Withdraw consent from receiving communications.</li>
        </ul>
        <p>
          To exercise these rights, contact us at{" "}
          <a href="mailto:mgbwworks@gmail.com">mgbwworks@gmail.com</a>
        </p>

        <h2>8. Changes to This Policy</h2>
        <p>
          We may update this Privacy Policy from time to time. Updates will be
          posted on this page.
        </p>

        <h2>9. Contact Us</h2>
        <p>
          MGBW Group<br />
          Email: <a href="mailto:mgbwworks@gmail.com">mgbwworks@gmail.com</a><br />
          Phone: 0821-2420241<br />
          Address: Head Office, Vinoba Road, Mysore-570005
        </p>
      </div>
    </section>
  );
}
